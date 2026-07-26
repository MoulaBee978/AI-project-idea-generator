# AI Project Idea Generator - Setup & Run Guide

## Quick Start

This is a complete AI Project Idea Generator built with:
- **Frontend**: React 18 + TypeScript + Tailwind CSS + Vite
- **Backend**: FastAPI + LangChain + Gemini API
- **LLM**: Google Gemini (free tier via API key)

## Prerequisites

1. **Node.js 18+** - Download from https://nodejs.org/
2. **Python 3.10+** - Download from https://www.python.org/
3. **Gemini API Key** - Get free from https://makersuite.google.com/app/apikey

## Setup Instructions

### Step 1: Get Your Gemini API Key

1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the API key

### Step 2: Set Up Backend

```bash
cd backend

# The virtual environment should already be created, but if not:
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies (if not already done)
pip install -r requirements.txt
```

### Step 3: Configure Backend Environment

Edit `backend/.env` and replace:
```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

with your actual Gemini API key:
```
GEMINI_API_KEY=ak_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 4: Set Up Frontend

```bash
cd frontend

# Install dependencies
npm install
```

## Running the Application

### Terminal 1: Start Backend (FastAPI Server)

```bash
cd backend

# Activate virtual environment (if not already active)
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Start FastAPI server
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Terminal 2: Start Frontend (Vite Dev Server)

```bash
cd frontend

# Start development server
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  press h to show help
```

### Step 5: Use the Application

1. Open your browser to **http://localhost:5173**
2. Fill in the form:
   - **Domain of Interest**: Select your domain (AI, Healthcare, Finance, etc.)
   - **Programming Language**: Choose your language (Python, JavaScript, etc.)
   - **Technology Stack**: Select tech stack (MERN, FastAPI, Django, etc.)
   - **Difficulty**: Choose level (Beginner, Intermediate, Advanced)
3. Click **"Generate Ideas"**
4. Wait for the AI to generate 3 project ideas
5. Review the suggestions with all details

## Project Structure

```
d:/agentic_ai/
├── backend/
│   ├── .env                 # Environment variables (CREATE from .env.example)
│   ├── .env.example         # Example env file
│   ├── requirements.txt      # Python dependencies
│   ├── main.py              # FastAPI entry point
│   ├── chains/              # LangChain chain implementations
│   │   └── idea_chain.py    # Main idea generation chain
│   ├── prompts/             # AI prompt templates
│   │   └── idea_prompt.py   # Project idea prompt
│   ├── routes/              # API endpoint definitions
│   │   └── generate.py      # /api/generate-projects endpoint
│   ├── services/            # Business logic services
│   │   ├── gemini_client.py # Gemini API HTTP client
│   │   ├── langchain_service.py # LangChain service wrapper
│   │   └── vector_store.py  # ChromaDB integration (optional)
│   ├── models/              # Pydantic data models
│   │   └── project_models.py
│   └── utils/               # Utility functions
│       ├── output_parser.py # JSON parser for LLM output
│       └── lcel_wrapper.py  # LCEL expression helpers
│
├── frontend/
│   ├── src/
│   │   ├── main.tsx         # React entry point
│   │   ├── App.tsx          # Main app component
│   │   ├── index.css        # Tailwind styles
│   │   └── components/      # React components
│   │       ├── InputForm.tsx    # User input form
│   │       └── ProjectCard.tsx  # Project display card
│   ├── index.html           # HTML template
│   ├── package.json         # Node.js dependencies
│   ├── tsconfig.json        # TypeScript config
│   ├── vite.config.ts       # Vite config
│   ├── tailwind.config.cjs  # Tailwind CSS config
│   └── postcss.config.cjs   # PostCSS config
│
├── README.md                # Project documentation
└── SETUP_AND_RUN.md        # This file
```

## Troubleshooting

### "GEMINI_API_KEY is required in environment"
- Make sure you've created `backend/.env` file
- Make sure you've added your actual Gemini API key (not the placeholder)
- Try restarting the backend server

### Port 8000 already in use
```bash
# Kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :8000
kill -9 <PID>
```

### Port 5173 already in use
```bash
# Use a different port:
npm run dev -- --port 5174
```

### ImportError: No module named 'fastapi'
- Make sure virtual environment is activated
- Run: `pip install -r requirements.txt`

### npm: command not found
- Install Node.js from https://nodejs.org/

### Python version too old (< 3.10)
- Install Python 3.10+ from https://www.python.org/

## LangChain Features Used

✅ **PromptTemplate** - Custom prompts for project idea generation  
✅ **ConversationBufferMemory** - Maintains conversation history  
✅ **JSONOutputParser** - Parses and validates LLM JSON output  
✅ **LCEL Wrapper** - Lightweight expression language for utilities  
✅ **Modular Chains** - Organized `IdeaChain` class handling generation logic  

## API Endpoints

### Health Check
```
GET /health
Response: {"status": "ok"}
```

### Generate Project Ideas
```
POST /api/generate-projects
Body: {
  "domain": "Artificial Intelligence",
  "language": "Python",
  "tech_stack": "FastAPI",
  "difficulty": "Intermediate"
}
Response: {
  "projects": [
    {
      "title": "...",
      "problem_statement": "...",
      "objective": "...",
      "why_useful": "...",
      "required_technologies": [...],
      "recommended_stack": "...",
      "key_features": [...],
      "learning_outcomes": [...],
      "future_enhancements": [...],
      "estimated_time": "...",
      "best_suitable_for": "..."
    },
    ...
  ]
}
```

## Production Deployment

For production deployment:
1. Set `GEMINI_API_KEY` as an environment variable (not in `.env`)
2. Build frontend: `npm run build` (creates `dist/` folder)
3. Serve frontend from a static file server (Nginx, Vercel, etc.)
4. Run backend with a production ASGI server (Gunicorn, etc.)

## Support

- **Gemini API Issues**: https://ai.google.dev/
- **LangChain Docs**: https://langchain.readthedocs.io/
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **React Docs**: https://react.dev/

---

**Happy coding! 🚀**
