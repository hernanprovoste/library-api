from fastapi import FastAPI
from routers import books, authors, auth

app = FastAPI(
    title="Library API",
    description="A simple API for a library",
    version="1.0.0",
)

app.include_router(books.router)
app.include_router(authors.router)
app.include_router(auth.router)



@app.get("/")
def read_root():
    return {"message": "Welcome to library api."}
