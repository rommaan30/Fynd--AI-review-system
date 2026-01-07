from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routes import reviews

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Review Backend",
    version="1.0"
)


# ✅ CORS CONFIG (THIS FIXES YOUR ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        # Next.js dev
    ],
    allow_credentials=True,
    allow_methods=["*"],  # POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "backend running",
        "docs": "/docs"
    }

app.include_router(reviews.router)
