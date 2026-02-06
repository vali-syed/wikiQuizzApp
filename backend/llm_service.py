import os
from bs4 import ParserRejectedMarkup
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

import json
import re

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    api_key=os.getenv("OPENAI_API_KEY")
)

#quizz prompt 
quiz_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
You are an AI tutor.

Generate 5 multiple-choice questions from the article content below.

Rules:
- Questions must be strictly based on the content.
- Each question must have 4 options.
- Provide correct answer.
- Provide difficulty level (easy, medium, hard).
- Provide a short explanation.

Return STRICT JSON only in this format:
[
  {{
    "question": "",
    "options": [],
    "answer": "",
    "difficulty": "",
    "explanation": ""
  }}
]

Article content:
{content}
"""
)

def parse_quiz_json(raw_text: str):
    # Remove ```json and ``` wrappers
    cleaned = re.sub(r"```json|```", "", raw_text).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return None

#quiz generation using gpt 4o
def generate_quiz(article_content: str):
    prompt = quiz_prompt.format(content=article_content)
    response = llm.invoke(prompt)
    return parse_quiz_json(response.content)

#related topics generation
def generate_related_topics(article_content:str):
    prompt = f"""Suggest 5 related wikipedia topucs based on this article summary.
        return a json array of string
        
        Text:{article_content[:1000]}
        """
    response = llm.invoke(prompt)
    return parse_quiz_json(response.content)

# extracting related entities
def extract_entities(article_content: str):
    prompt = f"""
Extract key entities from the text.

Return STRICT JSON:
{{
  "people": [],
  "organizations": [],
  "locations": []
}}


Text:
{article_content}
"""
    response = llm.invoke(prompt)
    return parse_quiz_json(response.content)
