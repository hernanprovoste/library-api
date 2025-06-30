from pydantic import BaseModel
from typing import List, Optional

# Schemas for Author
class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

# Schemas for Book
class BookBase(BaseModel):
    title: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author: Author # Anidamos el schema del author

    class Config:
        orm_mode = True