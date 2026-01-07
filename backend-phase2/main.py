from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Hard CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Force OPTIONS handling for ALL routes
@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    return Response(status_code=200)
