from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Data Analyst Agent is running 🚀"}