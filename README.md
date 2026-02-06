# WikiQuiz App

A web application that generates quiz questions from Wikipedia articles using AI. Enter any Wikipedia URL and get multiple choice questions to test your knowledge.

## Tech Stack

### Backend
- FastAPI - Web framework for building APIs
- SQLAlchemy - Database ORM
- SQLite - Database
- LangChain - AI framework
- OpenAI GPT-4o-mini - AI model for quiz generation
- BeautifulSoup - Web scraping
- Uvicorn - ASGI server

### Frontend
- HTML
- CSS
- JavaScript

## Features

- Scrape Wikipedia articles by URL
- Generate multiple choice quiz questions from article content
- AI-powered question generation with difficulty levels
- View quiz history of previously generated articles
- Extract key entities like people, organizations, and locations
- Get related topic suggestions
- Store articles and quizzes in database

## How to Run Locally

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the backend directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

6. Run the server:
   ```
   uvicorn main:app --reload
   ```

The backend will run on `http://127.0.0.1:8000`

### Frontend Setup

1. Open the `frontend/index.html` file in your web browser
2. Or use a local server:
   - Python:
     ```
     cd frontend
     python -m http.server 8001
     ```
   - Then open `http://localhost:8001` in your browser

### Using the Application

1. Open the frontend in your browser
2. Enter a Wikipedia article URL in the input field
3. Click Generate to create quiz questions
4. View your quiz history in the Past Quizzes tab

## Screenshots

### Quiz Generation View
<img width="1920" height="1200" alt="Screenshot 2026-02-06 103915" src="https://github.com/user-attachments/assets/6af137d3-0f02-42d8-bd05-2a9d4d046008" />

### Quiz History View
<img width="1920" height="1200" alt="Screenshot 2026-02-06 103930" src="https://github.com/user-attachments/assets/94889890-f289-4f01-b948-6cc73ffecc22" />

## Project Structure

```
WikiQuizzApp/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── models.py         # Database models
│   ├── database.py       # Database configuration
│   ├── scrapper.py       # Wikipedia scraping
│   ├── llm_service.py    # AI quiz generation
│   ├── schemas.py        # Pydantic schemas
│   ├── requirements.txt  # Python dependencies
│   └── quiz.db           # SQLite database
├── frontend/
│   └── index.html        # Frontend application
└── README.md
```

## API Endpoints

- `GET /` - Health check
- `GET /articles` - Get all articles
- `POST /articles` - Create article from Wikipedia URL
- `POST /articles/{article_id}/quiz` - Generate quiz for an article
