from datetime import timedelta
from typing import Annotated, List
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
import base64
import uuid
import os

from PIL import Image

import shutil
router = APIRouter()

oauth2_scheme_2 = OAuth2PasswordBearer("/api")
#db = Databa_bases_2.conexion_directa()
RUTA_CARPETA = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_validar/firmas/"  # Ruta donde se guardará la imagen
# --- Modelo de entrada para guardar imagen ---
class ImagenBase64(BaseModel):
    imagen: str  # Formato esperado: 'data:image/png;base64,...'




@router.post("/api/devolver")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):

    # token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    # user_name =  token_decode.get("sub")
    # exp = token_decode.get("exp")
    # code =  token_decode.get("code")
    
    # tiempo = datetime.utcfromtimestamp(exp)
    # tiempo_2 = tiempo-timedelta(minutes=10)
    # now = datetime.utcnow()+timedelta()
    # # print(now)
    # if now > tiempo_2:
    #          raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

    # try:
    #     token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    #     user_name =  token_decode.get("sub")
    #     code =  token_decode.get("code")
    #     exp = token_decode.get("exp")

    #     tiempo = datetime.utcfromtimestamp(exp)
    #     now = datetime.utcnow()+timedelta()

    #     if user_name == None:
    #          raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except jwt.ExpiredSignature:
    #      raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:
            contents = await input.form()


            
            DIRECION_0 = os.getenv('DIRECION_0')

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            direcion_plazo =  contents["direcion_plazo"]
            query = """
            SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
            FROM folders f
            LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS ASIGNADOS ASESORA' and s.active = True
            ORDER BY f.id, s.created_at DESC;
            """
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            numero_orden_regitrado = cursor.fetchall()
            carpeta_raiz = numero_orden_regitrado[0][0]
            sub_carpeta  = numero_orden_regitrado[0][1]
            direcion_original = str("plazos_sejec/{}/{}/").format(carpeta_raiz, sub_carpeta)
            direcion_plazo_fina =  direcion_plazo.replace(direcion_original, "")
            conn.close()
            cursor.close()
            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
            except OSError:
                os.remove(path)

            #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            
            dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/'+direcion_plazo_fina
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + direcion_plazo
            shutil.copy(directorio_doc, dirercion_archvios_2)#copiar el archvio

            documento_inf  = guardar_evento(contents, direcion_plazo_fina)

            
            contenido = os.listdir(dirercion_archvios)
            try:
                        # comprecion de archivos 
                for x in contenido:
                    dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/'+x
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
                    shutil.copy(dirercion_archvios_2, directorio_doc)

                    documento_eliminar = [documento_inf[0]]
                    directorio_doc_eliminar = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop{}".format(documento_inf[1],direcion_plazo_fina)
                    for doc in documento_eliminar:
                        path = os.path.join(directorio_doc_eliminar, doc)
                        try:
                            shutil.rmtree(path)
                        except OSError:
                            os.remove(path)

            except OSError as e:
                print("Error de archivo: {}".format(e))
            #asignados
            dato={
                "respuesta":"Orden Asignada con Exito"
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato



@router.post("/api/asignar_orden")
async def guardar_imagen(input: Request, token: str = Depends(oauth2_scheme_2)):

    # token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    # user_name =  token_decode.get("sub")
    # exp = token_decode.get("exp")
    # code =  token_decode.get("code")
    
    # tiempo = datetime.utcfromtimestamp(exp)
    # tiempo_2 = tiempo-timedelta(minutes=10)
    # now = datetime.utcnow()+timedelta()
    # # print(now)
    # if now > tiempo_2:
    #          raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

    # try:
    #     token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    #     user_name =  token_decode.get("sub")
    #     code =  token_decode.get("code")
    #     exp = token_decode.get("exp")

    #     tiempo = datetime.utcfromtimestamp(exp)
    #     now = datetime.utcnow()+timedelta()

    #     if user_name == None:
    #          raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except jwt.ExpiredSignature:
    #      raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:

    #try:
        # 1. Leer el cuerpo de la solicitud
        body  = await input.form()


        DIRECION_0 = os.getenv('DIRECION_0')
        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        direcion_plazo =  body["direcion_plazo"]
        query = """
        SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
        FROM folders f
        LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS ASIGNADOS ASESORA' and s.active = True
        ORDER BY f.id, s.created_at DESC;
        """
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        numero_orden_regitrado = cursor.fetchall()
        carpeta_raiz = numero_orden_regitrado[0][0]
        sub_carpeta  = numero_orden_regitrado[0][1]
        direcion_original = str("plazos_sejec/{}/{}/").format(carpeta_raiz, sub_carpeta)
        direcion_plazo_fina =  direcion_plazo.replace(direcion_original, "")
        conn.close()
        cursor.close()
        try:
            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_validar/documentos/'
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                        shutil.rmtree(path)
                except OSError:
                        os.remove(path)
                
        except OSError:
            os.remove(path)

        dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_validar/documentos/'+direcion_plazo_fina
        directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + direcion_plazo
        shutil.copy(directorio_doc, dirercion_archvios_2)#copiar el archvio


        documento_inf  = guardar_evento_asignar(body, direcion_plazo_fina)


        contenido = os.listdir(dirercion_archvios)
        try:
                        # comprecion de archivos 
            for x in contenido:
                dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_validar/documentos/'+x
                directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
                shutil.copy(dirercion_archvios_2, directorio_doc)

                documento_eliminar = [documento_inf[0]]
                directorio_doc_eliminar = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop{}".format(direcion_original)
                for doc in documento_eliminar:
                        path = os.path.join(directorio_doc_eliminar, doc)
                        try:
                            shutil.rmtree(path)
                        except OSError:
                            os.remove(path)

        except OSError as e:
                print("Error de archivo: {}".format(e))

        return {
            "mensaje": "Imagen guardada exitosamente",
        }

    #except Exception as e:
        #print(e)
        #raise HTTPException(status_code=500, detail=f"Error al guardar imagen: {str(e)}")

@router.post("/api/leer_orden_validar")
async def leer_orden(input: Request, token: str =  Depends(oauth2_scheme_2)):

    # token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    # user_name =  token_decode.get("sub")
    # exp = token_decode.get("exp")
    # code =  token_decode.get("code")
    
    # tiempo = datetime.utcfromtimestamp(exp)
    # tiempo_2 = tiempo-timedelta(minutes=10)
    # now = datetime.utcnow()+timedelta()
    # # print(now)
    # if now > tiempo_2:
    #          raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

    # try:
    #     token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    #     user_name =  token_decode.get("sub")
    #     code =  token_decode.get("code")
    #     exp = token_decode.get("exp")

    #     tiempo = datetime.utcfromtimestamp(exp)
    #     now = datetime.utcnow()+timedelta()

    #     if user_name == None:
    #          raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except jwt.ExpiredSignature:
    #      raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:



            documento_inf  = numero_orden_select()



            dato={
                 "ordenes_sin_asignadas":documento_inf[0],
             }
            
            return dato

@router.post("/api/leer_orden_orfeo")
async def leer_orden_orfeo(input: Request, token: str =  Depends(oauth2_scheme_2)):

    # token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    # user_name =  token_decode.get("sub")
    # exp = token_decode.get("exp")
    # code =  token_decode.get("code")
    
    # tiempo = datetime.utcfromtimestamp(exp)
    # tiempo_2 = tiempo-timedelta(minutes=10)
    # now = datetime.utcnow()+timedelta()
    # # print(now)
    # if now > tiempo_2:
    #          raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

    # try:
    #     token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    #     user_name =  token_decode.get("sub")
    #     code =  token_decode.get("code")
    #     exp = token_decode.get("exp")

    #     tiempo = datetime.utcfromtimestamp(exp)
    #     now = datetime.utcnow()+timedelta()

    #     if user_name == None:
    #          raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except jwt.ExpiredSignature:
    #      raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:


            contents = await input.form()
            documento_inf  = numero_orden_select_ver(contents)

            dato={
                 "tabla_log":documento_inf[0],
                "unidad_que_lidera":documento_inf[1],
                "unidad_que_apoya":documento_inf[2],
                "unidad_que_cordina":documento_inf[3],
                "nivel_prioridad_list":documento_inf[4],
                "nivel_autoridad_list":documento_inf[5],
                "sop_estado_mayor_list":documento_inf[6]
             }
            
            return dato



app = FastAPI(title="DIROP",
              description="api para el manejo de los resultados",
              version='1.0.1')

origins = [
"*",
]
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import uvicorn
IP = os.getenv('IP')

PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("ordenes_sejec_validar:app", port=PUERTO+47, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





