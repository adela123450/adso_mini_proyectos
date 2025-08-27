import os
import pathlib
os.environ["DB_PATH"] = str(pathlib.Path(__file__).parent / "test_tasks.db")

from fastapi.testclient import TestClient
from src.app import app, init_db

client = TestClient(app)
init_db()

def test_create_and_list():
    # Crear una tarea
    r = client.post("/tasks", json={"title": "Aprender FastAPI", "done": False})
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "Aprender FastAPI"

    # Listar y verificar que está
    r = client.get("/tasks")
    assert r.status_code == 200
    items = r.json()
    assert any(t["title"] == "Aprender FastAPI" for t in items)
