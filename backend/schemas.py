from pydantic import BaseModel

class ArticleCreate(BaseModel):
    url:str