from fastapi import FastAPI

app = FastAPI(title="docker-for-ai-engineers")


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/health")
def health():
    return {"status": "ok"}
