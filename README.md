# AI Project Idea Generator

This repository contains a full-stack AI Project Idea Generator using LangChain and Gemini. The backend is built with FastAPI and LangChain, and the frontend is a React + TypeScript app styled with Tailwind CSS.

Features
- Tailored project idea generation based on Domain, Language, Tech Stack, and Difficulty
- LangChain modular chains, prompt templates, output parsing, and conversation memory
- Gemini API for AI generation with free-tier support
- Modern dark themed UI with glassmorphism cards and smooth interactions

Tech stack
- Frontend: React, TypeScript, Vite, Tailwind CSS
- Backend: FastAPI, LangChain, Gemini, Python
- Optional: ChromaDB for persisting ideas

Project structure
- frontend/ - React app
- backend/ - FastAPI app and LangChain code

Getting started

Prerequisites
- Python 3.10+
- Node 18+
- Gemini API access (set `GEMINI_API_KEY` environment variable)

Gemini model
1. Obtain a Gemini API key from Google Cloud (free tier or IAM as applicable).
2. Set `GEMINI_API_KEY` in `backend/.env` or your environment.

You can optionally set `GEMINI_MODEL` to the desired model name (default `gemini-1.5`).

Backend setup

```bash
cd backend
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env if needed
uvicorn backend.main:app --reload
```

Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Usage
- Open the frontend (typically http://localhost:5173) and fill the form.
- Click "Generate Ideas" and wait for the backend to call the Gemini API.

Notes
- This project uses a Gemini REST client to generate project ideas via the Gemini API.
- Set `GEMINI_API_KEY` in `backend/.env` or your environment, and optionally customize `GEMINI_MODEL`.


Future improvements
- Add caching and a ChromaDB-backed vector store to save previously generated ideas
- Add user accounts and saved collections
- Add unit/integration tests and CI automation
