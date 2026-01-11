from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas

# -------------------------------------------------------------------
# Application
# -------------------------------------------------------------------

app = FastAPI(
    title="Task API",
    description="API de gestion de tâches (FastAPI + PostgreSQL + Docker)",
    version="1.0.0",
)

# -------------------------------------------------------------------
# Initialisation de la base de données
# -------------------------------------------------------------------

Base.metadata.create_all(bind=engine)

# -------------------------------------------------------------------
# Routes de base
# -------------------------------------------------------------------

@app.get("/", tags=["Health"])
def health_check():
    """
    Vérifie que l'API est opérationnelle.
    """
    return {"status": "ok", "message": "Task API is running"}

# -------------------------------------------------------------------
# Routes Tasks
# -------------------------------------------------------------------

@app.post(
    "/tasks",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    """
    Crée une nouvelle tâche.
    """
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get(
    "/tasks",
    response_model=list[schemas.Task],
    tags=["Tasks"],
)
def list_tasks(db: Session = Depends(get_db)):
    """
    Retourne toutes les tâches.
    """
    return db.query(models.Task).all()


@app.get(
    "/tasks/{task_id}",
    response_model=schemas.Task,
    tags=["Tasks"],
)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Récupère une tâche par son ID.
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Tasks"],
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Supprime une tâche.
    """
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()
    return None
