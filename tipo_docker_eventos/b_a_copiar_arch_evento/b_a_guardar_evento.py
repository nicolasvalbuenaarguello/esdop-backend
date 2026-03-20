from __init__ import *

import os

router = APIRouter()

#importaciones a modulos propios

import os
import shutil


app = FastAPI(title="DIROP",
              description="api para el manejo de los eventos negativos",
              version='1.0.2')


IP_SEGURITY = os.getenv('IP_SEGURITY')
# IP_SEGURITY =  ["http://localhost:4200"]
# origins = [
# "*",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=IP_SEGURITY,
    allow_credentials=True,
    expose_headers=[],
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.post("/api")
async def guardar(datos : Request):

    contents = await datos.form()
    #archivos
    direcion_r =contents["link"]
    nombre =contents["nombre"]

    DIRECION_4 = os.getenv('DIRECION_4')
    DIRECION_5 = os.getenv('DIRECION_5')


        
    #descarga de archivos 
    for files in os.listdir(DIRECION_4):
        path = os.path.join(DIRECION_4, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


    link = DIRECION_5 + nombre
    directorio_doc = DIRECION_4
    directorio= direcion_r
    shutil.copy(directorio, directorio_doc)
    print(link)
    dato={
         "link":link
    }
    # print("guardar evento")
    return link
app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))
print("guardar evento")
if __name__ == "__main__":
     config = uvicorn.Config("b_a_guardar_evento:app", port=PUERTO+32, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

