from __init__ import *
from  a_a_guardar_evento.models.guaradar_evento.guardar_evento import *
from  a_a_guardar_evento.models.guaradar_evento.reporte_respueta import *
from  a_b_planilla.models_2.planilla_conceptos.plnaillas import *
from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()
from correo.correo import *

APP_PATH = os.getcwd()

router = APIRouter()

#importaciones a modulos propios

app = FastAPI(title="DIROP",
              description="api para el manejo de los resultados",
              version='1.0.1')

origins = [
"*",
]
IP_SEGURITY = os.getenv('IP_SEGURITY')
SECRETE_KEY = os.getenv('SECRETE')
ALGORITHM = os.getenv('ALGORITHM')

app.add_middleware(
    CORSMiddleware,
    allow_origins=IP_SEGURITY,
    allow_credentials=True,
    expose_headers=[],
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme_2 = OAuth2PasswordBearer("/")
db = Databa_bases_2.conexion_directa()


#-----------------------------------------
#---ANOTACIONES BOLETIN OPERACINAL--------
#-----------------------------------------

@router.post("/url_cargar_afectaciones_q5")
async def url_cargar_afectaciones_q5(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =ingreso_anotacion_operacional(contents)

        
        dato={
            "respuesta":"evento Guardado"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_afectaciones_listado_q5")
async def url_afectaciones_listado_q5(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos
    
        donmbre_archivo =anotaciones_registro_boletines(contents)

        
        dato={
            "listado_q5_afectaciones":donmbre_archivo[0],
 
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_descargar_eventos_relevante")
async def descargar_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        try:
            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente/'
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
            
            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/'
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
        except OSError:
            os.remove(path)
            

        #crear hoja de datos y guardar
        id =contents["id"]
        if id =="":
            documento = informe_pendiente(contents)
        else:
              documento = informe_pendiente_id(contents)
        dato={
            "nombre":documento[1],
            "link":documento[0]
        }
        #print(dato)
        # print("guardar evento")
        return dato

app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("tipo_q5_afectaciones:app", port=PUERTO+15, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

