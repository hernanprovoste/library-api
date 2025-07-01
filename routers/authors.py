from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import models, schemas
from database.database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

@router.post("/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@router.get("/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = db.query(models.Author).offset(skip).limit(limit).all()
    return authors

@router.get("/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found.")
    return db_author