import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.api.routes import
from app.core.logging import setup_logging

# Setup logging
setup_logging()

app = FastAPI(
    title="Verbaflo FAQ API",
    description="API for managing and searching FAQs",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# app.include_router(router)

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Template FASTAPI",
        "version": "1.0.0"
    }

# For local deployement
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)