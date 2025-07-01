from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import models, schemas
from database.database import get_db

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # Verifica si el autor existe
    db_author = db.query(models.Author).filter(models.Author.id == book.author_id).first()
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book