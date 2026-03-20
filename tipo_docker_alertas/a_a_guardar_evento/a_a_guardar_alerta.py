from __init__ import *
from models.guaradar_evento.guardar_evento import *


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

@router.post("/guardar")
async def guardar(datos: Request, token: str =  Depends(oauth2_scheme_2)):

    # token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    # print(token_decode.get("exp"))

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

    #     # tiempo = datetime.utcfromtimestamp(exp)

    #     if user_name == None:
    #          raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except JWTError:
    #     raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    # except JWTError.ExpiredSignatureError:
    #      raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
    
    # user = User(user_name = user_name )
    # logged_user = ModelUser.loguin(db, user)

    # if not logged_user:
    #      raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

    # if user.disabled:
    #       raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
    # else:
         
    # #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#producci

        contents = await datos.form()
        #archivos


        acta_alerta = contents["acta_alerta"]
        acta_alerta_2 = contents["acta_alerta_2"]

        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        dirercion_archvios = '{}tipo_docker_alertas/a_a_guardar_evento/documentos/'.format(ruta)

        if acta_alerta_2 =="---":
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
            if acta_alerta != "---": 
                acta_alerta_nombres =contents["acta_alerta"].filename
                with open(getcwd() + "/documentos/"+str(acta_alerta_nombres), "wb")as myfile:
                    hechos = await acta_alerta.read()
                    myfile.write(hechos)
                    myfile.close()
            else:
                acta_alerta_nombres=acta_alerta_2
        else:
                acta_alerta_nombres="validar"


        # comprecion de archivos 
        documento_inf  = guardar_evento(contents, acta_alerta_nombres)

                            
        if acta_alerta_2 == "---":
            raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = '{}tipo_docker_alertas/a_a_guardar_evento/documentos/'.format(ruta)
            # arcivos a la ruta final 
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[1]
            directorio= dirercion_archvios_2+acta_alerta_nombres
            shutil.copy(directorio, directorio_doc)

        dato={
            "respuesta":"Alerta Guardada con Exito",
            "alertas":documento_inf[0]
        }
        # print(dato)
        # print("guardar evento")
        return dato

@router.post("/eliminar")
async def eliminar_alerta(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos


        # comprecion de archivos 
        documento_inf  = eliminar(contents)

        acta_reserva_ruta = contents["alerta_scaneada"]
        # print(foto)

        DIRECION_0 = os.getenv('DIRECION_0')
        ruta = DIRECION_0

        dirercion_archvios_3 = ruta + acta_reserva_ruta
        # print(dirercion_archvios_3)
        if acta_reserva_ruta !="-//-":                                
            try:
                    # print(dirercion_archvios_3)
                os.remove(dirercion_archvios_3) 
            except OSError as e:
                print("Error de archivo: {}".format(e))


        dato={
            "respuesta":"Se elimino la Aelrta con Exito",
            "alertas":documento_inf[0]
        }
        # print(dato)
        # print("guardar evento")
        return dato


@router.post("/editar")
async def editar_alerta(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos


        # comprecion de archivos 
        documento_inf  = eliminar(contents)


        acta_reserva_ruta = contents["alerta_scaneada"]
        # print(foto)

        DIRECION_0 = os.getenv('DIRECION_0')
        ruta = DIRECION_0
                
        acta_alerta = contents["acta_alerta"]
        acta_alerta_2 = contents["acta_alerta_2"]

        dirercion_archvios_3 = ruta + acta_reserva_ruta
        # print(dirercion_archvios_3)
        if acta_alerta_2 =="---":                                
            try:
                    # print(dirercion_archvios_3)
                os.remove(dirercion_archvios_3) 
            except OSError as e:
                print("Error de archivo: {}".format(e))


        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        dirercion_archvios = '{}usuarios/documentos'.format(ruta)
        #dirercion_archvios = '{}tipo_docker_alertas/a_a_guardar_evento/documentos'.format(ruta)

        if acta_alerta_2 =="---":
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
            if acta_alerta != "---": 
                acta_alerta_nombres =contents["acta_alerta"].filename
                with open(getcwd() + "/documentos/"+str(acta_alerta_nombres), "wb")as myfile:
                    hechos = await acta_alerta.read()
                    myfile.write(hechos)
                    myfile.close()
            else:
                acta_alerta_nombres=acta_alerta_2
        else:
                acta_alerta_nombres="validar"


        # comprecion de archivos 
        documento_inf  = guardar_evento(contents, acta_alerta_nombres)

                            
        if acta_alerta_2 == "---":
            raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = '{}tipo_docker_alertas/a_a_guardar_evento/documentos/'.format(ruta)
            # arcivos a la ruta final 
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[1]
            directorio= dirercion_archvios_2+acta_alerta_nombres
            shutil.copy(directorio, directorio_doc)


        dato={
            "respuesta":"Se edito la Alerta con Exito",
            "alertas":documento_inf[0]
        }
        # print(dato)
        # print("guardar evento")
        return dato

app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("a_a_guardar_alerta:app", port=PUERTO+33, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

