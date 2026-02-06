from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import engine,get_db

from models import Base,Article
from schemas import ArticleCreate
from scrapper import scrape_wikipedia
from llm_service import generate_quiz,generate_related_topics,extract_entities
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for now
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, etc
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def checking():
    return {"backend check":'backend running'}

@app.get("/articles")
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()

    return [
        {
            "id": a.id,
            "title": a.title,
            "url": a.url
        }
        for a in articles
    ]

@app.post('/articles')
def create_article(
    data:ArticleCreate,
    db:Session = Depends(get_db)
):
    #scrape the article 
    scraped = scrape_wikipedia(data.url)

    if not scraped:
        return {"error":"Failed to scrape article"}

    # saving the article to db 

    article = Article(
        url=data.url,
        title=scraped["title"],
        summary=scraped["content"][:2000]
    )

    db.add(article)
    db.commit()
    db.refresh(article)
 
    return {
        "id":article.id,
        "url":article.url,
        "title":article.title
    }


@app.post("/articles/{article_id}/quiz")
def generate_article_quiz(
    article_id: int,
    db: Session = Depends(get_db)
):
    article = db.query(Article).filter(Article.id == article_id).first()

    if not article:
        return {"error": "Article not found"}

    quiz = generate_quiz(article.summary)

    related_topics = generate_related_topics(article.summary)

    key_entities = extract_entities(article.summary)

    return {
        "article_id": article.id,
        "title": article.title,
        "url":article.url,
        "quiz": quiz,
        "key_entities":key_entities or {
            "people": [],
            "organizations": [],
            "locations": []
            },
        "related_topics":related_topics or []
    }
