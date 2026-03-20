from __init__ import *
from  a_a_guardar_evento.models.guaradar_evento.guardar_evento import *
from  a_a_guardar_evento.models.guaradar_evento.reporte_respueta import *
from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()
from correo.correo import *

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

#modulo de copiado de plazos sin asignar 
@router.post("/plazos")
async def guardar(datos: Request, token: str =  Depends(oauth2_scheme_2)):

    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
            
            contents = await datos.form()
            #archivos

            contenido = os.listdir('Z:/DIROP/0000 PLAZOS/SIN ASIGNAR')

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}tipo_aetcr/a_a_guardar_evento/documentos'.format(ruta)
            


            try:
                        # comprecion de archivos 
                for x in contenido:

                    #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = 'Z:/DIROP/0000 PLAZOS/SIN ASIGNAR/'+x
                    #arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/sin_asignar/" + x
                    
                    shutil.move(dirercion_archvios_2, directorio_doc)

                contenido_2 = os.listdir('C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/sin_asignar')
            except OSError as e:
                print("Error de archivo: {}".format(e))


            dato={
                "respuesta":"AETCR Guardada con Exito",
                "plazos":contenido_2,

            }

            return dato

    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

#modulo de asignacion de plazos 
@router.post("/asignacion")
async def asigancion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
        
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
            
        
            contents = await datos.form()
            #archivos
            documento =  contents["documento"]
            correo_ejc =  contents["correo_ejc"]
            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                
            #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+documento
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/sin_asignar/" + documento
                    
            shutil.move(directorio_doc, dirercion_archvios_2)# comprecion de archivos 
            #crear hoja de datos y guardar
            donmbre_archivo =listado(contents)
            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
            

            contenido = os.listdir(dirercion_archvios)
            #file = open("Z:/COE/SS VALBUENA/correo.txt","w")
            #file.write(correo_ejc)
            #file.close()
            #f = open("Z:/COE/SS VALBUENA/correo.txt", "r")
            #('r’) opens the text files for reading only
            #mi_correro = f.read()
            #f.close()
            try:
                        # comprecion de archivos 
                for x in contenido:
                    
                    
                    #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+x

                    #enviar_correo(correo_ejc, dirercion_archvios_2, x)
                    #arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    
                    shutil.move(dirercion_archvios_2, directorio_doc)
                    dirercion_archvios_2 = 'Z:/DIROP/0000 PLAZOS/ASIGNADOS/'+x
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    shutil.copy(directorio_doc, dirercion_archvios_2)

            except OSError as e:
                print("Error de archivo: {}".format(e))
            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato

    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

#modulo de eliminacion de plazos 
@router.post("/eliminar_easignacion_url")
async def eliminacion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
            

            contents = await datos.form()
            #archivos
            documento =  contents["documento_pdf"]
            
            #id

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                
            #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/documento_eliminar.pdf'
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento
                    
            shutil.move(directorio_doc, dirercion_archvios_2)# comprecion de archivos 
            #crear hoja de datos y guardar
            donmbre_archivo = elimnar_asignacion(contents)

            
            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
            
            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato

    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})


@router.post("/reasignacion_url")
async def reasigancion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
    print("----")
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        
    
            contents = await datos.form()
            #archivos
            documento =  contents["documento_pdf"]
            correo_ejc =  contents["correo_ejc"]
            #id

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                
            #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/documento_eliminar.pdf'
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento
            directorio_doc_z = directorio_doc
            shutil.copy(directorio_doc, dirercion_archvios_2)# comprecion de archivos 
    
            #crear hoja de datos y guardar
            donmbre_archivo = listado_reasiganr(contents)
            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
            

            contenido = os.listdir(dirercion_archvios)
            #file = open("Z:/COE/SS VALBUENA/correo.txt","w")
            #file.write(correo_ejc)
            #file.close()
            #f = open("Z:/COE/SS VALBUENA/correo.txt", "r")
            #('r’) opens the text files for reading only
            #mi_correro = f.read()
            #f.close()
            try:
                        # comprecion de archivos 
                for x in contenido:
                    
                    
                    #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+x

                    #enviar_correo(correo_ejc, dirercion_archvios_2, x)
                    #arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    dirercion_archvios_2_z = dirercion_archvios_2
                    shutil.copy(dirercion_archvios_2, directorio_doc)
                    dirercion_archvios_2 = 'Z:/DIROP/0000 PLAZOS/ASIGNADOS/'+x
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    shutil.copy(directorio_doc, dirercion_archvios_2)
                    os.remove(dirercion_archvios_2_z)
                    os.remove(directorio_doc_z)
                    

            except OSError as e:
                print("Error de archivo: {}".format(e))
            
            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato


    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

@router.post("/cumplir_easignacion_url_respuesta")
async def cumplir_easignacion_url_respuesta(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:

            contents = await datos.form()
            #archivos
            
            cumplido_soporte =  contents["cumplido_soporte"]
            cumplido_soporte_2 =  contents["cumplido_soporte_2"]

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
            

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}usuarios/documentos'.format(ruta)
            #dirercion_archvios = '{}tipo_docker_alertas/a_a_guardar_evento/documentos'.format(ruta)

            if cumplido_soporte_2 =="---":
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                if cumplido_soporte != "---": 
                    cumplido_soporte_nombres =contents["cumplido_soporte"].filename
                    with open(getcwd() + "/a_a_guardar_evento/documentos/"+str(cumplido_soporte_nombres), "wb")as myfile:
                        hechos = await cumplido_soporte.read()
                        myfile.write(hechos)
                        myfile.close()
                else:
                    cumplido_soporte_nombres=cumplido_soporte_2
            else:
                    cumplido_soporte_nombres="validar"

            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
            

            nombre_documento = cimplimiento_plazo_respuesta(contents, cumplido_soporte_nombres)

            contenido = os.listdir(dirercion_archvios)

    
            try:
                        # comprecion de archivos 
                for x in contenido:
                    
                    #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+x

                    #enviar_correo(correo_ejc, dirercion_archvios_2, x)
                    #arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/respuestas/" + x
                    
                    shutil.move(dirercion_archvios_2, directorio_doc)
                    #dirercion_archvios_2 = 'Z:/DIROP/0000 PLAZOS/ASIGNADOS/'+x

                    #directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    #shutil.copy(directorio_doc, dirercion_archvios_2)

            except OSError as e:
                print("Error de archivo: {}".format(e))
            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato


    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})


@router.post("/actualizar_asunto_url")
async def actualizar_asunto_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        
            contents = await datos.form()
            #archivos

            nombre_documento = actualizar_asunto(contents)
                    #directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    #shutil.copy(directorio_doc, dirercion_archvios_2)


            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato

    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})


@router.post("/cumplir_easignacion_url")
async def plazo_cumplido(datos: Request, token: str =  Depends(oauth2_scheme_2)):
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        
            contents = await datos.form()
            #archivos
            documento =  contents["documento_pdf"]
            cumplido_soporte =  contents["cumplido_soporte"]
            cumplido_soporte_2 =  contents["cumplido_soporte_2"]


            #id

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
            

            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            dirercion_archvios = '{}usuarios/documentos'.format(ruta)
            #dirercion_archvios = '{}tipo_docker_alertas/a_a_guardar_evento/documentos'.format(ruta)

            if cumplido_soporte_2 =="---":
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                if cumplido_soporte != "---": 
                    cumplido_soporte_nombres =contents["cumplido_soporte"].filename
                    with open(getcwd() + "/a_a_guardar_evento/documentos/"+str(cumplido_soporte_nombres), "wb")as myfile:
                        hechos = await cumplido_soporte.read()
                        myfile.write(hechos)
                        myfile.close()
                else:
                    cumplido_soporte_nombres=cumplido_soporte_2
            else:
                    cumplido_soporte_nombres="validar"

            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
            

            #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
            dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/documento_inicial.pdf'
            directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop" + documento

            directorio_doc_f = directorio_doc
                    
            shutil.copy(directorio_doc, dirercion_archvios_2)# comprecion de archivos 
            #crear hoja de datos y guardar



            nombre_documento = cimplimiento_plazo(contents, cumplido_soporte_nombres)

            contenido = os.listdir(dirercion_archvios)

    
            try:
                        # comprecion de archivos 
                for x in contenido:
                    
                    #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+x

                    #enviar_correo(correo_ejc, dirercion_archvios_2, x)
                    #arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/completados/" + x
                    
                    shutil.copy(dirercion_archvios_2, directorio_doc)
                    os.remove(dirercion_archvios_2)
                    os.remove(directorio_doc_f)
                    #dirercion_archvios_2 = 'Z:/DIROP/0000 PLAZOS/ASIGNADOS/'+x

                    #directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/asignados/" + x
                    #shutil.copy(directorio_doc, dirercion_archvios_2)

            except OSError as e:
                print("Error de archivo: {}".format(e))
            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato



    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

@router.post("/plazos_asignados_url")
async def plazos_asignados_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):

    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
    
            contents = await datos.form()
            #archivos

            
            contenido_2 =buscar(contents)


            dato={

                "plazos_asignados":contenido_2[0]

            }

            return dato

    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})


@router.post("/plazos_asignados_url_seguimiento")
async def plazos_asignados_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        

            contents = await datos.form()
            #archivos

            
            contenido_2 =buscar_2(contents)


            dato={

                "plazos_asignados_pendientes":contenido_2[0]

            }

            return dato



    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

@router.post("/creacion_plazo_url")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        

            contents = await datos.form()
            #archivos

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/creacion_plazos_documentos/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/creacion_plazos_documentos_qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                


            #crear hoja de datos y guardar
            crear_plazo(contents)



            dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/creacion_plazos_documentos/'
            

            contenido = os.listdir(dirercion_archvios)

    
            try:
                        # comprecion de archivos 
                for x in contenido:
                    
                    
                    #raiz= "tipo_docker_eventos/a_a_guardar_evento/documentos".format(ruta)
                    dirercion_archvios_2 = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/creacion_plazos_documentos/'+x

                    #enviar_correo(correo_ejc, dirercion_archvios_2, x)
                    #arcivos a la ruta final 
                    directorio_doc = "C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos/sin_asignar/" + x
                    
                    shutil.move(dirercion_archvios_2, directorio_doc)

            except OSError as e:
                print("Error de archivo: {}".format(e))
            dato={
                "listado_aetcr":"documento_inf[0]"
            }
            #print(dato)
            # print("guardar evento")
            return dato


    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

@router.post("/reporte_pdf_respuesta_url")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        

            contents = await datos.form()
            #archivos

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                


            #crear hoja de datos y guardar
            documento = informe_pendiente(contents)

            dato={
                "nombre":documento[1],
                "link":documento[0]
            }
            #print(dato)
            # print("guardar evento")
            return dato


    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})


@router.post("/reporte_pdf_respuesta_url_estadistica")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        
    
            contents = await datos.form()
            #archivos

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                


            #crear hoja de datos y guardar
            documento = informe_pendiente_estadistica(contents)

            dato={
                "nombre":documento[1],
                "link":documento[0]
            }
            #print(dato)
            # print("guardar evento")
            return dato


    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
 
@router.post("/reporte_pdf_respuesta_url_balance")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
    try:
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        # print(token_decode.get("exp"))

        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")
        code =  token_decode.get("code")
        tiempo = datetime.utcfromtimestamp(exp)
        tiempo_2 = tiempo-timedelta(minutes=10)
        now = datetime.utcnow()+timedelta()
        # print(now)
        if now > tiempo_2:
                raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        try:
            token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            user_name =  token_decode.get("sub")
            code =  token_decode.get("code")
            exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            if user_name == None:
                raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        except JWTError.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        user = User(user_name = user_name )
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        if user.disabled:
            raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        else:
        

            contents = await datos.form()
            #archivos

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)
                


            #crear hoja de datos y guardar
            informe_pendiente(contents)
            informe_pendiente_estadistica(contents)
            documento = balance(contents)

            try:
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
                
                dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/'
                for files in os.listdir(dirercion_archvios):
                    path = os.path.join(dirercion_archvios, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            except OSError:
                os.remove(path)

            dato={
                "nombre":documento[1],
                "link":documento[0]
            }
            #print(dato)
            # print("guardar evento")
            return dato



    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})



app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("a_plazos:app", port=PUERTO+8, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

