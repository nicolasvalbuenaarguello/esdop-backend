from datetime import timedelta
from typing import Annotated, List
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form

router = APIRouter()

oauth2_scheme_2 = OAuth2PasswordBearer("/api")
db = Databa_bases_2.conexion_directa()

@router.post("/guardar")
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
            foto =contents["foto"]

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}tipo_docker_personal/usuarios/fotos'.format(ruta)

            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)

            if foto != "---":  
                foto_name =contents["foto"].filename
                with open(getcwd() + "/fotos/"+str(foto_name), "wb")as myfile:
                    hechos = await foto.read()
                    myfile.write(hechos)
                    myfile.close()
            else:
                foto_name=foto
                
            documento_inf  = guardar_evento(contents, foto_name)

            # raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = '{}tipo_docker_personal/usuarios/fotos/'.format(ruta)

            # arcivos a la ruta final 
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
            directorio= dirercion_archvios_2+"/"+foto_name
            shutil.copy(directorio, directorio_doc)
            
            dato={
                "respuesta":"Personal Guardado con Exito",
                "listado_personal":documento_inf[1], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato
@router.post("/update")
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
    # except jose.exceptions.ExpiredSignatureError:
    #     raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:
            
            
            contents = await input.form()
            documento_inf  = delete_evento(contents)
            # print("llegue")
            foto_ruta = contents["foto_ruta"]
            foto = contents["foto"]
            foto_2 = contents["foto_2"]
            
            # print(foto)

            DIRECION_0 = os.getenv('DIRECION_0')
            ruta = DIRECION_0

            dirercion_archvios_2 = ruta + foto_ruta
            # print(dirercion_archvios_2)
            if foto_2 =="---":
                remove(dirercion_archvios_2)
            # dato={
            #     "respuesta":"Personal Eliminado con Exito",
            #     "usuarios":documento_inf[0], 
            # }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
        

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}tipo_docker_personal/usuarios/fotos'.format(ruta)

            if foto_2 =="---":
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)

                if foto != "---":  
                    foto_name =contents["foto"].filename
                    with open(getcwd() + "/fotos/"+str(foto_name), "wb")as myfile:
                        hechos = await foto.read()
                        myfile.write(hechos)
                        myfile.close()
                else:
                    foto_name=foto
            else:
                 foto_name="validar"
                
            documento_inf  = guardar_evento_update(contents, foto_name)

            # raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = '{}tipo_docker_personal/usuarios/fotos/'.format(ruta)

            # arcivos a la ruta final 
            if foto_2 =="---":
                directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
                directorio= dirercion_archvios_2+"/"+foto_name
                shutil.copy(directorio, directorio_doc)
            
            dato={
                "respuesta":"Personal Editado con Exito",
                "listado_personal":documento_inf[1], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }

            return dato

@router.post("/eliminar")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):
    
           
            contents = await input.form()
            documento_inf  = delete_evento(contents)
            delete_cargo_personal(contents)
            # print("llegue")
            foto_ruta = contents["foto_ruta"]
            # print(foto_ruta)

            DIRECION_0 = os.getenv('DIRECION_0')
            ruta = DIRECION_0

            dirercion_archvios_2 = ruta + foto_ruta
            # print(dirercion_archvios_2)
            remove(dirercion_archvios_2)
            dato={
                "respuesta":"Personal Eliminado con Exito",
                "listado_personal":documento_inf[0], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato

@router.post("/eliminar_cargo")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):
    
           
            contents = await input.form()
            documento_inf = delete_cargo_personal_unico(contents)

            dato={
                "respuesta":"---",
                "cargo_personal":documento_inf[0], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato

@router.post("/select_cargo")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):
    
           
            contents = await input.form()
            documento_inf = select_cargo_personal(contents)

            dato={
                "respuesta":"----",
                "cargo_personal":documento_inf[0], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato


@router.post("/guardar_cargo")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):
    
           
            contents = await input.form()
            documento_inf = guardar_cargo(contents)

            dato={
                "respuesta":"----",
                "cargo_personal":documento_inf[0], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
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
     config = uvicorn.Config("personal:app", port=PUERTO+36, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





