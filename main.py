from fastapi import FastAPI

app = FastAPI(
    title="Library API",
    description="A simple API for a library",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Hello Library"}
