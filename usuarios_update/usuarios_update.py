from datetime import timedelta
from typing import Annotated, List

import jose
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form

router = APIRouter()

oauth2_scheme_2 = OAuth2PasswordBearer("/api")
db = Databa_bases_2.conexion_directa()

@router.post("/api/user")
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
        

    #     # if datetime.utcnow() > token_decode.expires:
    #     #     raise HTTPException(status_code=403, detail="token has been expired")
        
    
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except jose.ExpiredSignatureError: # <---- this one
    #     raise HTTPException(status_code=403, detail="token has been expired")
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:
            contents = await input.form()
            
            foto_ruta = contents["foto_ruta"]
            foto_2 = contents["foto_2"]
            foto = contents["foto"]

            acta_reserva_file = contents["acta_reserva_file"]
            acta_reserva_ruta = contents["acta_reserva_ruta"]
            acta_reserva_2 = contents["acta_reserva_2"]
            
            DIRECION_0 = os.getenv('DIRECION_0')
            ruta = DIRECION_0

        #---  gestion de foto   ---#
            dirercion_archvios_2 = ruta + foto_ruta
            if foto_2 =="---":                                
                try:
                    os.remove(dirercion_archvios_2) 
                except OSError as e:
                    print("Error de archivo: {}".format(e))
                    
            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}usuarios_update/fotos'.format(ruta)

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
        #---  gestion de foto   ---#
#------------------------------ // -------------------------------------------
        #---  gestion de documento   ---#
            ruta = DIRECION_0
            dirercion_archvios_3 = ruta + acta_reserva_ruta
            # print(dirercion_archvios_3)
            if acta_reserva_2 =="---":                                
                try:
                    os.remove(dirercion_archvios_3) 
                except OSError as e:
                    print("Error de archivo: {}".format(e))
                    
            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}usuarios_update/documentos'.format(ruta)

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
        #---  gestion de documento   ---#


            documento_inf  = update_evento(contents, foto_name, acta_reserva_file_nombres)

            if foto_2 =="---":
                raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                dirercion_archvios_2 = '{}usuarios_update/fotos/'.format(ruta)
                # arcivos a la ruta final 
                directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
                directorio= dirercion_archvios_2+foto_name
                shutil.copy(directorio, directorio_doc)
                
            if acta_reserva_2 =="---":
                raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                dirercion_archvios_2 = '{}usuarios_update/documentos/'.format(ruta)
                # arcivos a la ruta final 
                directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[1]
                directorio= dirercion_archvios_2+acta_reserva_file_nombres
                shutil.copy(directorio, directorio_doc)

            dato={
                "respuesta":"Usuario Guardado con Exito",
                "usuarios":documento_inf[2], 
            }
            return dato
    
@router.post("/api/update")
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
            foto = contents["foto"]

            acta_reserva_ruta = contents["acta_reserva_ruta"]
            # print(foto)

            DIRECION_0 = os.getenv('DIRECION_0')
            ruta = DIRECION_0

            dirercion_archvios_2 = ruta + foto
            # print(dirercion_archvios_2)
            remove(dirercion_archvios_2)

            dirercion_archvios_3 = ruta + acta_reserva_ruta
            # print(dirercion_archvios_3)
            if acta_reserva_ruta !="---":                                
                try:
                    # print(dirercion_archvios_3)
                    os.remove(dirercion_archvios_3) 
                except OSError as e:
                    print("Error de archivo: {}".format(e))

            dato={
                "respuesta":"Usuario Eliminado con Exito",
                "usuarios":documento_inf[0], 
            }
            # dato={
            #     "respuesta":"Usuario Guardado con Exito",
            # }
            
            return dato
   
    
@router.post("/cambiar_contrasena")
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
            documento_inf  = cambio_contrasena(contents)
            # print("llegue")
 

            print(documento_inf)
            
            return documento_inf
   

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
     config = uvicorn.Config("usuarios_update:app", port=PUERTO+197, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





