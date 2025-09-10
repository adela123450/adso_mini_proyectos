[![tests](https://github.com/adela123450/adso_mini_proyectos/actions/workflows/ci.yml/badge.svg?branch=principal)](https://github.com/adela123450/adso_mini_proyectos/actions/workflows/ci.yml)

# Mini-proyectos  (FastAPI)

Este repositorio contiene **2 mini-proyectos** listos para revisión técnica:
- **01_api_sqlite** — API CRUD (Create/Read/Update/Delete) con **FastAPI** y **SQLite** + **pytest** (pruebas).
- **02_nlp_fastapi** — Mini NLP (limpieza/tokenización de texto con **NLTK**) expuesto como API **FastAPI** + **pytest**.

## Cómo correr rápido (local)
> Requiere Python 3.x

### 1) API CRUD + SQLite
```bash
cd 01_api_sqlite
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn src.app:app --host 127.0.0.1 --port 8001 --reload
# Docs: http://127.0.0.1:8001/docs
# Pruebas: pytest -q

cd 02_nlp_fastapi
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn src.app:app --host 127.0.0.1 --port 8002 --reload
# Docs: http://127.0.0.1:8002/docs
# Pruebas: pytest -q

