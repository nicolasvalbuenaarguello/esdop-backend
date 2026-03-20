import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

# 🔥 CORRECCIÓN AQUÍ
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

load_dotenv()

from routers.consulta import router

app = FastAPI(title="DIROP - CENAM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        port=PUERTO + 142,
        host=IP,
        log_level="info",
        reload=True
    )
    server = uvicorn.Server(config)
    server.run()