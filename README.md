# NotebookLM Clone (Django + React)

This project is a simplified NotebookLM-like app where users upload PDFs and ask questions. The backend extracts per-page text, splits into chunks, embeds using OpenAI, stores vectors in FAISS, and answers questions with citations (page numbers). Frontend is a React (Vite) app with a PDF viewer and chat UI.

## Features
- Upload PDF
- Extract per-page text (PyMuPDF)
- Chunking with overlap
- OpenAI embeddings (text-embedding-3-small)
- FAISS local vector index
- Query endpoint: search and answer (gpt-4o-mini)
- PDF viewer with citation buttons that scroll to pages

## Prerequisites
- Python 3.10+
- Node.js 18+
- pip and npm
- OpenAI API key

## Setup (Windows - PowerShell)
```powershell
# Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Create .env from .env.example and set OPENAI_API_KEY
copy .env.example .env
# edit .env and paste OPENAI key
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Frontend (new shell)
cd frontend
npm install
# create .env file if needed: VITE_API_URL=http://127.0.0.1:8000/api
npm run dev
```

## Setup (Linux / macOS - bash)
```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

# Frontend (new terminal)
cd frontend
npm install
# optionally set VITE_API_URL
npm run dev
```

## Testing
1. Start backend and frontend.
2. Open frontend, upload a PDF.
3. Ask a question related to the PDF. The response will include page citations.
4. Click a citation button to jump to that page in the viewer.

## Notes & Caveats
- This is a **minimal** working scaffold. For production:
  - Use a proper vector DB (Pinecone, Qdrant) for scale.
  - Use cloud storage (S3) for PDFs.
  - Secure API keys and add authentication.
  - Improve error handling and batching of embedding calls.
