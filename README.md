# WikiQuiz App

A quiz application that generates questions from Wikipedia articles.

## Project Structure

```
WikiQuizzApp/
├── backend/          # FastAPI backend
│   ├── main.py      # FastAPI application entry point
│   ├── models.py    # Database models
│   ├── database.py  # Database configuration
│   ├── routers/     # API route handlers
│   ├── schemas/     # Pydantic schemas
│   ├── services/    # Business logic
│   └── requirements.txt
├── frontend/        # Frontend application
└── README.md
```

## Setup

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create `.env` file:
   ```env
   DATABASE_URL=sqlite:///./quiz.db
   SECRET_KEY=your-secret-key-here
   ```

6. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

(To be added when frontend is set up)

## Features

- Generate quiz questions from Wikipedia articles
- Multiple choice questions
- Score tracking
- Quiz history

## Technologies

- **Backend**: FastAPI, SQLAlchemy, Python
- **Frontend**: (To be determined)
