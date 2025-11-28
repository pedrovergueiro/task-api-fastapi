from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from app.routes import router

app = FastAPI(title="TaskMaster API")

# ========== CORS FIX ==========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # permite GET, POST, PATCH, DELETE, OPTIONS...
    allow_headers=["*"],  # permite JSON, Authorization, etc.
)
# =====================================

@app.on_event("startup")
def on_start():
    create_db_and_tables()

app.include_router(router)
