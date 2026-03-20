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


@router.post("/conceptos_medallas_descargar_url")
async def conceptos_medallas_descargar_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()

        print('---')


        LINK = os.getenv('DIRECION_3_B')
        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        link = LINK

        dirercion_archvios = link
        for files in os.listdir(dirercion_archvios):
            path = os.path.join(dirercion_archvios, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)



        documento_inf = excel(contents)
        


        #
        dato={
            "link":documento_inf[0],
            "nombre":documento_inf[1]
        }
        # print(dato)
        # print("guardar evento")
        return dato


@router.post("/conceptos_medallas_descargar_url")
async def conceptos_medallas_descargar_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()

        tipo =  contents["tipo"]
        
             
        dirercion_archvios = APP_PATH +"/a_b_planilla/documentos_conceptos/"
        try:

            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)

        except OSError:
            os.remove(path)

        if tipo == "CONCEPTOS":
            planillas(contents)
            documento_inf = combine_all_docx(contents)
        elif tipo == "LISTADO":
            documento_inf = informe_entrega(contents)


        dato={
            "link":documento_inf[0],
            "nombre":documento_inf[1]
        }
        # print(dato)
        # print("guardar evento")
        return dato


@router.post("/proyecto_guardar")
async def asigancion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =listado(contents)

        
        dato={
            "proyectos":donmbre_archivo[0]
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/creacion_medalla_url")
async def asigancion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =guardar_medalla(contents)

        
        dato={
            "radicado":donmbre_archivo[0],
            "dato":"Se Registro la Medalla"
        }
        #print(dato)
        # print("guardar evento")
        return dato

@router.post("/eliminar_medalla_url")
async def eliminar_medalla_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

        donmbre_archivo =elimnar_asignacion(contents)

        
        dato={
            "dato":"Se Registro la Medalla"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/listado_inicial_medallas_url")
async def plazos_asignados_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):

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
            "proyectos":contenido_2[0], 
             "radicado":contenido_2[1]
        }

        return dato


@router.post("/listado_personal_medallas_url")
async def plazos_asignados_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):

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

        
        contenido_2 =listado_medallas(contents)


        dato={
            "listado_medallas":contenido_2[0], 
            "proyectos":contenido_2[1],
            "unidades_label":contenido_2[2],
            "medalla_label":contenido_2[3],
            "estado_medalla_label":contenido_2[4]
        }

        return dato

        # comprecion de archivos 
        

@router.post("/conceptos_medallas_url")
async def reasigancion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()

        tipo =  contents["tipo"]
        
             
        dirercion_archvios = APP_PATH +"/a_b_planilla/documentos_conceptos/"
        try:

            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)

        except OSError:
            os.remove(path)

        if tipo == "CONCEPTOS":
            planillas(contents)
            documento_inf = combine_all_docx(contents)
        elif tipo == "LISTADO":
            documento_inf = informe_entrega(contents)


        dato={
            "link":documento_inf[0],
            "nombre":documento_inf[1]
        }
        # print(dato)
        # print("guardar evento")
        return dato

@router.post("/registro_estado_proyecto_medalla_url")
async def registro_estado_proyecto_medalla_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

 
        actulizar_informacion_estado_medalla(contents)

        
        dato={
            "update":"se regitro la informacion"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/registro_editar_informacion_url")
async def registro_editar_informacion_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

 
        actulizar_informacion_medallas(contents)

        
        dato={
            "update":"se regitro la informacion"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/registro_difab_medalla_url")
async def registro_difab_medalla_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
        contents = await datos.form()
        #archivos

 
        actulizar_informacion_difab(contents)

        
        dato={
            "update":"se regitro la informacion"
        }
        #print(dato)
        # print("guardar evento")
        return dato


@router.post("/eliminar_easignacion_url")
async def eliminacion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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

@router.post("/reasignacion_url")
async def reasigancion(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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
                
        shutil.move(directorio_doc, dirercion_archvios_2)# comprecion de archivos 
        #crear hoja de datos y guardar
        donmbre_archivo = listado_reasiganr(contents)
        dirercion_archvios = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'
        

        contenido = os.listdir(dirercion_archvios)
        file = open("Z:/COE/SS VALBUENA/correo.txt","w")
        file.write(correo_ejc)
        file.close()
        f = open("Z:/COE/SS VALBUENA/correo.txt", "r")
        #('r’) opens the text files for reading only
        mi_correro = f.read()
        f.close()
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

@router.post("/cumplir_easignacion_url")
async def plazo_cumplido(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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
                
        shutil.move(directorio_doc, dirercion_archvios_2)# comprecion de archivos 
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

@router.post("/plazos_asignados_url_seguimiento")
async def plazos_asignados_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):

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

        
        contenido_2 =buscar_2(contents)


        dato={

            "plazos_asignados_pendientes":contenido_2[0]

        }

        return dato

@router.post("/creacion_plazo_url")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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

@router.post("/reporte_pdf_respuesta_url")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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

@router.post("/reporte_pdf_respuesta_url_estadistica")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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

@router.post("/reporte_pdf_respuesta_url_balance")
async def creacion_plazo_url(datos: Request, token: str =  Depends(oauth2_scheme_2)):
       
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


app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("a_medallas:app", port=PUERTO+9, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

