import base64
from datetime import timedelta
from io import BytesIO
from tkinter import Image
from typing import Annotated, List
import uuid
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form
from PIL import Image
router = APIRouter()



oauth2_scheme_2 = OAuth2PasswordBearer("/api/crear_user_url")
#db = Databa_bases_2.conexion_directa()
RUTA_CARPETA = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/usuarios_sejec/firmas/"  # Ruta donde se guardará la imagen

     
@router.post("/api/crear_user_url")
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

            # 1. Leer el cuerpo de la solicitud
            body  = await input.form()

            foto =body["foto"]

            DIRECION_0 = os.getenv('DIRECION_0')

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}usuarios_sejec/fotos'.format(ruta)

            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)

            if foto != "---":  
                foto_name =body["foto"].filename
                with open(getcwd() + "/fotos/"+str(foto_name), "wb")as myfile:
                    hechos = await foto.read()
                    myfile.write(hechos)
                    myfile.close()
            else:
                foto_name=foto
            
            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION


            documento_inf  = guardar_evento(body, foto_name)

            if foto_name != "---":
                raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                dirercion_archvios_2 = '{}usuarios_sejec/fotos/'.format(ruta)

                # arcivos a la ruta final 
                directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
                directorio= dirercion_archvios_2+"/"+foto_name
                shutil.copy(directorio, directorio_doc)

            
            dato={
                "respuesta":"Usuario Guardado con Exito",
                "usuarios_sejec":documento_inf[1], 
                
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato

@router.post("/api/cargo_sejec")
async def cargo_sejec(input: Request, token: str =  Depends(oauth2_scheme_2)):


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
            documento_inf  = guardar_cargos(contents)



            
            dato={
                  "respuesta":"Cargo creado con Éxito",
                "cargos_sejec":documento_inf[0], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato

     
@router.post("/api/editar_permisos_usuarios")
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
            body  = await input.form()
            imagen_str = body["imagen"] 
            nombre_archivo = body["nombre_archivo"]  # Opcional
            firma_numero  = body["firma_numero"]  # firma_numero

            guardar_imagen = True
 
            if nombre_archivo == "no imagen" or imagen_str == "no imagen":
                guardar_imagen = False

            if guardar_imagen:
                # Validar formato base64
                if not imagen_str or not imagen_str.startswith("data:image/png;base64,"):
                    raise HTTPException(status_code=400, detail="Formato de imagen inválido o no proporcionado")

                # Generar nombre si no fue enviado
                if not nombre_archivo:
                    nombre_archivo = f"imagen_{uuid.uuid4().hex[:8]}.png"

                # Limpiar carpeta de destino
                try:
                    if os.path.exists(RUTA_CARPETA):
                        shutil.rmtree(RUTA_CARPETA)
                    os.makedirs(RUTA_CARPETA, exist_ok=True)
                except Exception as e:
                    raise HTTPException(status_code=500, detail=f"Error al preparar la carpeta: {e}")

                # Procesar y guardar imagen
                try:
                    imagen_base64 = imagen_str.split(",")[1]
                    imagen_bytes = base64.b64decode(imagen_base64)
                    ruta_final = os.path.join(RUTA_CARPETA, nombre_archivo)

                    with Image.open(BytesIO(imagen_bytes)) as im:
                        im.save(ruta_final)

                        # Guardar copia con nombre de firma
                        nombre_firma = f"{firma_numero}_firma.png"
                        ruta_firma = os.path.join(RUTA_CARPETA, nombre_firma)
                        im.save(ruta_firma)
                except Exception as e:
                    raise HTTPException(status_code=400, detail=f"Error al guardar imagen: {e}")

            # 🚀 Aquí continúa el resto de la lógica del endpoint

            documento_inf  = eidtar_permisos_user(body, guardar_imagen)
            
            if guardar_imagen:
                DIRECION = os.getenv('DIRECION')
                ruta = DIRECION
                dirercion_archvios_2 = '{}usuarios_sejec/firmas/'.format(ruta)

                # arcivos a la ruta final 
                directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[1]
                directorio= dirercion_archvios_2+"/"+nombre_firma
                shutil.copy(ruta_firma, directorio_doc)

            dato={
                "respuesta":"Usuario Editado con Exito",
                "usuarios_sejec":documento_inf[0], 
                
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato


import uvicorn
IP = os.getenv('IP')

PUERTO = int(os.getenv('PUERTO'))

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
if __name__ == "__main__":
     config = uvicorn.Config("usuarios_creacion_sejec:app", port=PUERTO+41, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





