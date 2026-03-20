from datetime import timedelta
from typing import Annotated, List
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form

router = APIRouter()

oauth2_scheme_2 = OAuth2PasswordBearer("/api")
#db = Databa_bases_2.conexion_directa()
def connect():
    conn = psycopg2.connect(" \
        dbname=PLAZOS_SEGUNDO_CDTE \
        user=postgres \
        password=NICval10**")
    return conn

@router.post("/api/crear_plazo")
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
            acta_reserva_file = contents["acta_reserva_file"]
            acta_reserva_2 = contents["acta_reserva_2"]
            DIRECION_0 = os.getenv('DIRECION_0')
            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}ordenes_sejec/fotos'.format(ruta)
            query = """
            SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
            FROM folders f
            LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS SIN ASIGNAR' and s.active = True
            ORDER BY f.id, s.created_at DESC;
            """
            conn = connect()
            cursor = conn.cursor()
            cursor.execute(query)
            numero_orden_regitrado = cursor.fetchall()

            if numero_orden_regitrado:

                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)


                DIRECION = os.getenv('DIRECION')
                ruta = DIRECION
                dirercion_archvios = '{}ordenes_sejec/documentos'.format(ruta)

                if acta_reserva_2 =="---":
                    for files in os.listdir(dirercion_archvios):
                        path = os.path.join(dirercion_archvios, files)
                        try:
                            shutil.rmtree(path)
                        except OSError:
                            os.remove(path)
                    if acta_reserva_file != "---": 
                        acta_reserva_file_nombres =contents["acta_reserva_file"].filename
                        with open(getcwd() + "/documentos/"+str(acta_reserva_file_nombres), "wb")as myfile:
                            hechos = await acta_reserva_file.read()
                            myfile.write(hechos)
                            myfile.close()
                    else:
                        acta_reserva_file_nombres=acta_reserva_2
                else:
                    acta_reserva_file_nombres="validar"

                documento_inf  = guardar_evento(contents, acta_reserva_file_nombres)

                raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                dirercion_archvios_2 = '{}usuarios/fotos/'.format(ruta)

                # arcivos a la ruta final 
                
                                
                if acta_reserva_2 =="---":
                    raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = '{}ordenes_sejec/documentos/'.format(ruta)
                    # arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
                    directorio= dirercion_archvios_2+acta_reserva_file_nombres
                    shutil.copy(directorio, directorio_doc)
                
                dato={
                    "respuesta":"Plazo Creado con Exito"
                }
                # dato={
                #     "respuesta":"Usuario Guardado con Exito",
                # }
                
                return dato
            else:
                dato={
                    "error":"no hay carpetas creadas donde se va a guardar los archivos, si eres usuario por favor comunicarse con el administrador, si eres root crear las carpetas"
                }
                # dato={
                #     "respuesta":"Usuario Guardado con Exito",
                # }
                
                return dato
                 

@router.post("/api/leer_orden")
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
                 "numero_orden":documento_inf[0],
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
     config = uvicorn.Config("ordenes_secej:app", port=PUERTO+42, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





