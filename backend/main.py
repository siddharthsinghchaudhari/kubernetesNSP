from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def hello():
    return {"message": "Hello from FastAPI backend after a git commit!"}
