from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

# ✅ IMPORT YOUR ROUTER
from routes.reviews import router as review_router  # adjust filename if different

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ OPTIONS handler
@app.options("/{path:path}")
async def options_handler(path: str):
    return Response(status_code=200)

# ✅ Health check
@app.get("/")
def health():
    return {"status": "ok"}

# ✅ REGISTER ROUTES
app.include_router(review_router)
