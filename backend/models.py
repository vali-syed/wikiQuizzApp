from sqlalchemy import Column,Integer,String,ForeignKey,JSON
from database import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer,primary_key=True)
    url = Column(String)
    title = Column(String)
    summary = Column(String)

class QuizQuestion(Base):
    __tablename__ = 'quiz_questions'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    question = Column(String)
    options = Column(JSON)
    answer = Column(String)
