from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

import uvicorn

app = FastAPI()

# ✅ CORS para que Angular pueda llamar sin bloqueo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o tu dominio Angular si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 📂 Carpeta donde están los archivos
DIRECTORIO = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/formatos_dicte"

@app.get("/descargar/{nombre}")
def descargar(nombre: str):
    ruta = os.path.join(DIRECTORIO, nombre)
    if not os.path.exists(ruta):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    # 🔥 Forzar descarga
    return FileResponse(
        ruta,
        filename=nombre,
        media_type="application/octet-stream"
    )

if __name__ == "__main__":
    config = uvicorn.Config(
        "servidor_archivos:app",
        host="0.0.0.0",
        port=5194,
        ssl_keyfile="clave.key",
        ssl_certfile="certificado.crt",
        log_level="info",
        reload=True
    )
    server = uvicorn.Server(config)
    server.run()
