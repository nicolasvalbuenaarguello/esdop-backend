import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sub_regiones
from models import models, database
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title="DIROP - Subregiones")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sub_regiones.router)  # ← YA NO LE DES EL PREFIX AQUÍ

# Lanza el servidor
import uvicorn
IP = os.getenv('IP')

PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("main:app", port=PUERTO+140, host=IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()
