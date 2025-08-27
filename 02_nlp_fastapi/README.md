# 02_nlp_fastapi — Mini NLP + API (FastAPI + NLTK)

Mini API que recibe un texto y devuelve **tokens** limpios (minúsculas, sólo letras, sin *stopwords*).

## Cómo ejecutar (Windows, Git Bash)
```bash
cd 02_nlp_fastapi
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn src.app:app --host 127.0.0.1 --port 8002 --reload

