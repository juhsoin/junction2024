from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def read_api():
    return {"message": "This is a mock API endpoint"}