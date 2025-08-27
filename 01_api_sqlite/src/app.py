import os
import sqlite3
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = os.getenv("DB_PATH", "tasks.db")

def _conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = _conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

class TaskIn(BaseModel):
    title: str
    done: bool = False

class TaskOut(TaskIn):
    id: int

app = FastAPI(title="API de Tareas (ADSO)")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks", response_model=TaskOut)
def create_task(task: TaskIn):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks(title, done) VALUES(?, ?)", (task.title, int(task.done)))
    conn.commit()
    tid = cur.lastrowid
    cur.execute("SELECT id, title, done FROM tasks WHERE id=?", (tid,))
    row = cur.fetchone()
    conn.close()
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks():
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, done FROM tasks ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r["id"], "title": r["title"], "done": bool(r["done"])} for r in rows]

@app.get("/tasks/{tid}", response_model=TaskOut)
def get_task(tid: int):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("SELECT id, title, done FROM tasks WHERE id=?", (tid,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}

@app.put("/tasks/{tid}", response_model=TaskOut)
def update_task(tid: int, task: TaskIn):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET title=?, done=? WHERE id=?", (task.title, int(task.done), tid))
    conn.commit()
    cur.execute("SELECT changes() as n")
    if cur.fetchone()["n"] == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    cur.execute("SELECT id, title, done FROM tasks WHERE id=?", (tid,))
    row = cur.fetchone()
    conn.close()
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}

@app.delete("/tasks/{tid}")
def delete_task(tid: int):
    conn = _conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (tid,))
    conn.commit()
    cur.execute("SELECT changes() as n")
    deleted = cur.fetchone()["n"]
    conn.close()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"deleted": True, "id": tid}
