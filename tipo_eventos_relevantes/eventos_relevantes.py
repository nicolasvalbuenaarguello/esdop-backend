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

@router.post("/url_cargar_eventos_relevante")
async def cargar_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =ingreso_evento_relavante(contents)

        
        dato={
            "respuesta":"evento Guardado"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_cargar_documentos_eventos_relevante")
async def cargar_documentos_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos


        documento_guardar = contents["documento_guardar"]
        documento_guardar_2 = contents["documento_guardar_2"]

        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        dirercion_archvios = '{}tipo_eventos_relevantes/a_a_guardar_evento/documentos/'.format(ruta)

        if documento_guardar_2 =="---":
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
            if documento_guardar != "---": 
                documento_guardar_nombres =contents["documento_guardar"].filename
                with open(getcwd() + "/a_a_guardar_evento/documentos/"+str(documento_guardar_nombres), "wb")as myfile:
                    hechos = await documento_guardar.read()
                    myfile.write(hechos)
                    myfile.close()
            else:
                documento_guardar_nombres=documento_guardar_2
        else:
                documento_guardar_nombres="validar"


        # comprecion de archivos 

        documento_inf =cargar_documento_evento_relavante(contents, documento_guardar_nombres)

                            
        if documento_guardar_2 == "---":
            raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = '{}tipo_eventos_relevantes/a_a_guardar_evento/documentos/'.format(ruta)
             #rcivos a la ruta final 
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento_inf[0]
            directorio= dirercion_archvios_2+documento_guardar_nombres
            shutil.copy(directorio, directorio_doc)
        
        
        dato={
            "respuesta":"evento Editado"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_editar_eventos_relevante")
async def editar_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =editar_evento_relavante(contents)

        
        dato={
            "respuesta":"evento Editado"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_ver_eventos_relevante")
async def ver_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =listado_eventos(contents)

        
        dato={
            "listado_eventos":donmbre_archivo[0],
 
        }
        #print(dato)
        # print("guardar evento")
        return dato

@router.post("/url_cargar_bitacora_eventos_relevante")
async def url_cargar_bitacora_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =ingreso_bitacora_evento_relavante(contents)

        
        dato={
            "dato":"Se Registro evento en la Bitacora"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_listado_bitacora_eventos_relevante")
async def url_listado_bitacora_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):

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

        
        contenido_2 =buscar(contents)


        dato={
            "bitacora":contenido_2[0], 
            "afectaciones":contenido_2[1], 
            "personal":contenido_2[2],
      
        }

        return dato


@router.post("/url_cargar_afectacion_eventos_relevante")
async def url_cargar_afectacion_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):

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

        
        ingresar_afectacion(contents)


        dato={
            "dato":"Se Registro la Afectacion"
        }

        return dato

        # comprecion de archivos 
        

@router.post("/url_editar_bitacora_eventos_relevante")
async def url_editar_bitacora_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()



        editar_bitacora_evento_relavante(contents)
  
  

        dato={
            "dato":"se edito la informacion de la bitacora",
        }
        # print(dato)
        # print("guardar evento")
        return dato

@router.post("/url_eliminar_bitacora_eventos_relevante")
async def url_eliminar_bitacora_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()



        eeliminar_bitacora_evento_relavante(contents)
  
  

        dato={
            "dato":"se elimino la informacion de la bitacora",
        }
        # print(dato)
        # print("guardar evento")
        return dato
@router.post("/url_eliminar_afectacion_eventos_relevante")
async def url_eliminar_afectacion_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()



        eeliminar_afectacion_evento_relavante(contents)
  
  

        dato={
            "dato":"se elimino la informacion de la bitacora",
        }
        # print(dato)
        # print("guardar evento")
        return dato


@router.post("/url_editar_afectacion_eventos_relevante")
async def url_editar_afectacion_eventos_relevante(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()



        editar_personal_afectado(contents)
  
  

        dato={
            "dato":"se edito la informacion de la bitacora",
        }
        # print(dato)
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
        divi_padre =contents["divi_padre"]
        departamento =contents["departamento"]

        if divi_padre != "" and divi_padre !="---":
              documento = informe_pendiente_division(contents)
        elif departamento != "" and departamento !="---":
              documento = informe_pendiente_departamento(contents)
        elif id =="":
            documento = informe_pendiente(contents)
              #documento = informe_pendiente_id(contents)
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
     config = uvicorn.Config("eventos_relevantes:app", port=PUERTO+12, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

