from typing import Annotated, List
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form
from fastapi import FastAPI, UploadFile, Form, Depends
from sqlalchemy import create_engine, text
import pandas as pd
import io
import datetime


import io
import pandas as pd
import traceback
from fastapi import APIRouter, UploadFile
from sqlalchemy import text


from fastapi import APIRouter, UploadFile, HTTPException



router = APIRouter()


#importaciones a modulos propios

app = FastAPI(title="DIROP",
              description="api para el manejo de los resultados",
              version='1.0.1')

origins = [
"*",
]

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


# 🔹 Conexión a PostgreSQL (ajusta credenciales)
DATABASE_URL = "postgresql://postgres:NICval10**@localhost:5432/dirop"
engine = create_engine(DATABASE_URL)




@router.post("/url_actualizar_inf_pasos_fronteras")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):


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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota


        contents = await input.form()
        pazos_fronterizos =contents["pazos_fronterizos_actulizar"]
        

        # input_json:UploadFile = File(input)
        # print(input.receive)
        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        dirercion_archvios = '{}pazos_fronterizos/documentos'.format(ruta)

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 

        for files in os.listdir(dirercion_archvios):
            path = os.path.join(dirercion_archvios, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

        # print(getcwd()+ "/server/documentos" )

        with open(getcwd() + "/documentos/plasos_fronterizos.xlsx", "wb")as myfile:
            archi_insitop_name = await pazos_fronterizos.read()
            myfile.write(archi_insitop_name)
            myfile.close()


        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()


        print("---x---")
        await cargar_resultados_pasos(contents)
        

        # await actualizar_datos()
        saludo = {
            'informacion_insitop':'Informacion Cargada en la base de Datos '
        }
        return saludo

@router.post("/url_cargar_inf_pasos_fronteras")
async def guarda_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):


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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota


        contents = await input.form()
        pazos_fronterizos =contents["pazos_fronterizos"]
        

        # input_json:UploadFile = File(input)
        # print(input.receive)
        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        dirercion_archvios = '{}pazos_fronterizos/documentos'.format(ruta)

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 

        for files in os.listdir(dirercion_archvios):
            path = os.path.join(dirercion_archvios, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

        # print(getcwd()+ "/server/documentos" )

        with open(getcwd() + "/documentos/plasos_fronterizos.xlsx", "wb")as myfile:
            archi_insitop_name = await pazos_fronterizos.read()
            myfile.write(archi_insitop_name)
            myfile.close()


        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()


        print("---x---")
        await cargar_resultados(contents)
        

        # await actualizar_datos()
        saludo = {
            'informacion_insitop':'Informacion Cargada en la base de Datos '
        }
        return saludo

@router.post("/url_ver_inf_pasos_fronteras")
async def url_ver_inf_pasos_fronteras(input: Request, token: str =  Depends(oauth2_scheme_2)):

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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota

        contents = await input.form()
        contentem = ver_inf_pasos_fronteras(contents)
        

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 



        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()



        

        # await actualizar_datos()
        dir = {
                "info_mapa_pasos":contentem[0],
            }
        return dir

@router.post("/url_ver_pasos_fronteras")
async def url_ver_pasos_fronteras(input: Request, token: str =  Depends(oauth2_scheme_2)):

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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota

        contents = await input.form()
        contentem = ver_pasos_fronteras(contents)
        

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 



        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()



        

        # await actualizar_datos()
        dir = {
                "info_mapa_pasos_directiva":contentem[0],
            }
        return dir


@router.post("/url_ver_reporte_pasos_fronteras")
async def url_ver_reporte_pasos_fronteras(input: Request, token: str =  Depends(oauth2_scheme_2)):

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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota

        contents = await input.form()
        documento = ver_reporte_pasos_fronteras(contents)

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 



        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()



        

        # await actualizar_datos()
        dato={
            "nombre":documento[1],
            "link":documento[0]
        }
        return dato


@router.post("/url_ver_inf_pasos_fronteras_dash")
async def url_ver_inf_pasos_fronteras_dash(input: Request, token: str =  Depends(oauth2_scheme_2)):

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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota

        contents = await input.form()
        documento = dash_reporte_pasos_fronteras(contents)

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 



        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()



        

        # await actualizar_datos()
        dato={
            "das_general":documento[0], 
            "dash_divisiones":documento[1],
            "dash_unidades":documento[2],
            "dash_label":documento[3]

        }
        return dato

@router.post("/guaradar_eleciones")
async def cargar_despliegue(file: UploadFile):
    try:
        # Leer Excel en memoria
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        # Normalizar nombres de columnas
        df.columns = [c.strip().lower() for c in df.columns]

        with engine.begin() as conn:
            # 🗑️ Borrar todos los registros antes de insertar
            conn.execute(text("TRUNCATE TABLE despliegue_unidades"))

            # ✅ Insertar fila por fila
            for i, row in df.iterrows():
                valores = {
                    "sigla_division": row.get("sigla_division"),
                    "sigla_brigada": row.get("sigla_brigada"),
                    "sigla_unidad": row.get("sigla_unidad"),
                    "compania": row.get("compania"),
                    "peloton": row.get("peloton"),
                    "comandante": row.get("comandante"),
                    "telefono": str(row.get("telefono")) if row.get("telefono") else None,
                    "oficiales": row.get("oficiales"),
                    "suboficiales": row.get("suboficiales"),
                    "soldados": row.get("soldados"),
                    "departamento": row.get("departamento"),
                    "municipio": row.get("municipio"),
                    "sitio": row.get("sitio"),
                    "puesto": row.get("puesto"),
                    "mesas": row.get("mesas"),
                    "potencial_electoral": row.get("potencial_electoral"),
                    "fecha_ocupacion": row.get("fecha_ocupacion"),
                    "fecha_repliegue": row.get("fecha_repliegue"),
                    "latitud": row.get("latitud"),
                    "longitud": row.get("longitud"),
                    "ejercito": row.get("ejercito"),
                    "policia": row.get("policia"),
                    "armada": row.get("armada"),
                    "fac": row.get("fac"),
                    "ej_ponal": row.get("ej_ponal"),
                    "ej_arc": row.get("ej_arc"),
                    "ponal_arc": row.get("ponal_arc"),
                    "ponal_fac": row.get("ponal_fac"),
                    "responsabilidad": row.get("responsabilidad"),
                    "observaciones": row.get("observaciones"),
                }

                conn.execute(text("""
                    INSERT INTO despliegue_unidades (
                        sigla_division, sigla_brigada, sigla_unidad, compania, peloton,
                        comandante, telefono, oficiales, suboficiales, soldados, departamento, municipio,
                        sitio, puesto, mesas, potencial_electoral, fecha_ocupacion, fecha_repliegue,
                        latitud, longitud, ejercito, policia, armada, fac, ej_ponal, ej_arc, ponal_arc, ponal_fac,
                        responsabilidad, observaciones
                    )
                    VALUES (
                        :sigla_division, :sigla_brigada, :sigla_unidad, :compania, :peloton,
                        :comandante, :telefono, :oficiales, :suboficiales, :soldados, :departamento, :municipio,
                        :sitio, :puesto, :mesas, :potencial_electoral, :fecha_ocupacion, :fecha_repliegue,
                        :latitud, :longitud, :ejercito, :policia, :armada, :fac, :ej_ponal, :ej_arc, :ponal_arc, :ponal_fac,
                        :responsabilidad, :observaciones
                    )
                """), valores)

        return {"status": "ok", "mensaje": "Datos cargados correctamente"}

    except Exception as e:
        return {"status": "error", "detalle": str(e)}

def dms_to_decimal(grados, minutos, segundos, hemisferio):
    try:
        if grados is None or str(grados).strip() == "":
            return None

        # Forzar a número (quita comas, espacios, etc.)
        g = float(str(grados).replace(",", ".").strip()) if pd.notna(grados) else 0
        m = float(str(minutos).replace(",", ".").strip()) if pd.notna(minutos) else 0
        s = float(str(segundos).replace(",", ".").strip()) if pd.notna(segundos) else 0

        decimal = g + (m / 60) + (s / 3600)

        if hemisferio in ["S", "W"]:
            decimal = -decimal

        return round(decimal, 8)
    except Exception:
        return None


@router.post("/cargar_mesas")
async def cargar_mesas(file: UploadFile):
    try:
        # Leer el archivo Excel
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        # Normalizar nombres de columnas
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # 🔹 Validar que existan todas las columnas esperadas
        columnas_esperadas = [
            "dd","mm","zz","pp","departamento","municipio","nombre_del_puesto",
            "mujeres","hombres","total_potencial","mesas","nombre_comuna_localidad",
            "direccion","lat_p","g_p","m_p","s_p","lon_p","g_p_l","m_p_l","s_p_l",
            "rural","urbana","ejercito_nacional","policia_nacional","armada_nacional",
            "cobertura","comunidad_indigena","division","brigada","batallon",
            "peloton","seccion","escuadra","indicativo","grado_cdte",
            "apellido_y_nombre_cdte_responsable_seguridad","numero_de_telefono_cdte",
            "lat","g_pr","m_pr","s_pr","lon","g_pr_l","m_pr_l","s_pr_l",
            "of","sub","slp","sl18","total","m","f","si","no","ponal","arc","fac"
        ]

        faltantes = [c for c in columnas_esperadas if c not in df.columns]
        if faltantes:
            raise HTTPException(status_code=400, detail=f"Faltan columnas: {faltantes}")

        # 🔹 Reemplazar NaN por valores vacíos
        df = df.fillna("")

        # 🔹 Limpiar la tabla antes de insertar
        with engine.begin() as conn:
            conn.execute(text("TRUNCATE TABLE puestos_votacion RESTART IDENTITY CASCADE"))

        # 🔹 Convertir tipos de columnas numéricas a int (si es posible)
        for col in ["mujeres","hombres","total_potencial","mesas","of","sub","slp","sl18","total","m","f","si","no"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

        # 🔹 Insertar los datos
        df.to_sql("puestos_votacion", con=engine, if_exists="append", index=False, method="multi")

        return {"status": "ok", "mensaje": f"Datos cargados correctamente: {len(df)} filas"}

    except Exception as e:
        print("🔥 ERROR REAL:", str(e))
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/cargar_reservas")
async def cargar_reservas(file: UploadFile):
    try:
        # Leer el archivo Excel
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        # Normalizar nombres de columnas para que coincidan con PostgreSQL
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # Esquema de columnas esperado en la tabla
        columnas_pg = [
            "departamento","municipio","lugar_de_ubicacion",
            "lat","lat_g","lat_m","lat_s",
            "lon","lon_g","lon_m","lon_s",
            "division","brigada","batallon","peloton","seccion",
            "indicativo","grado_cdte","apellido_y_nombre_cdte",
            "numero_de_telefono_cdte","of","sub","slp","sl18",
            "total","m","f","actividad"
        ]

        # Asegurar que el DataFrame tenga solo esas columnas
        df = df.reindex(columns=columnas_pg)

        # Limpiar la tabla antes de insertar (opcional)
        with engine.begin() as conn:
            conn.execute(text("TRUNCATE TABLE unidades_reserva RESTART IDENTITY CASCADE"))

        # Insertar en bloque
        df.to_sql("unidades_reserva", con=engine, if_exists="append", index=False, method="multi")

        return {"status": "ok", "mensaje": f"Datos cargados correctamente: {len(df)} filas"}

    except Exception as e:
        print("🔥 ERROR REAL:", str(e))
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/avance_cumplimiento")
async def cargar_avance_cumplimiento(file: UploadFile):
    try:
        # Leer el archivo Excel
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        # Normalizar nombres de columnas
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # Validar columnas esperadas
        columnas_esperadas = ["unidad", "puestos_comprometidos", "avance_cubrimientos", "porcentaje"]
        for col in columnas_esperadas:
            if col not in df.columns:
                raise HTTPException(status_code=400, detail=f"Falta la columna requerida: {col}")

        # Convertir porcentajes (pueden venir con coma decimal)
        df["porcentaje"] = (
            df["porcentaje"]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

        # Limpiar tabla antes de insertar
        with engine.begin() as conn:
            conn.execute(text("TRUNCATE TABLE resumen_divisiones RESTART IDENTITY CASCADE"))

        # Insertar en bloque
        df.to_sql("resumen_divisiones", con=engine, if_exists="append", index=False, method="multi")

        return {"status": "ok", "mensaje": f"Datos cargados correctamente: {len(df)} filas"}

    except Exception as e:
        print("🔥 ERROR REAL:", str(e))
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/cargue_divipol")
async def cargar_divipol(file: UploadFile):
    """
    Carga el archivo Excel de puestos de votación y lo inserta en la tabla diviplo.
    """
    try:
        # Leer el archivo Excel
        contents = await file.read()
        df = pd.read_excel(io.BytesIO(contents))

        # Normalizar nombres de columnas
        df.columns = [
            c.strip().lower()
            .replace(" ", "_")
            .replace("ó", "o")
            .replace("í", "i")
            .replace("ú", "u")
            .replace("ñ", "n")
            for c in df.columns
        ]

        # Validar columnas esperadas
        columnas_esperadas = [
            "dd", "mm", "zz", "pp", "departamen", "municipio", "puesto",
            "mujeres", "hombres", "total", "mesas", "comuna", "direccion",
            "latitud", "longitud", "tipo_de_pu", "unidad", "nombre_unidad"
        ]

        for col in columnas_esperadas:
            if col not in df.columns:
                raise HTTPException(status_code=400, detail=f"❌ Falta la columna requerida: {col}")

        # Limpiar y normalizar datos numéricos
        for campo in ["mujeres", "hombres", "total", "mesas"]:
            df[campo] = df[campo].fillna(0).astype(int)

        # Reemplazar comas por puntos en coordenadas y convertir a float
        df["latitud"] = df["latitud"].astype(str).str.replace(",", ".", regex=False).astype(float)
        df["longitud"] = df["longitud"].astype(str).str.replace(",", ".", regex=False).astype(float)

        # Crear tabla si no existe
        with engine.begin() as conn:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS diviplo (
                    id SERIAL PRIMARY KEY,
                    dd CHAR(2),
                    mm CHAR(3),
                    zz CHAR(2),
                    pp CHAR(2),
                    departamen VARCHAR(100),
                    municipio VARCHAR(100),
                    puesto VARCHAR(200),
                    mujeres INT,
                    hombres INT,
                    total INT,
                    mesas INT,
                    comuna VARCHAR(150),
                    direccion VARCHAR(200),
                    latitud DECIMAL(15,10),
                    longitud DECIMAL(15,10),
                    tipo_de_pu VARCHAR(20),
                    unidad VARCHAR(10),
                    nombre_unidad VARCHAR(100)
                );
            """))

            # Limpiar tabla antes de insertar
            conn.execute(text("TRUNCATE TABLE diviplo RESTART IDENTITY CASCADE"))

        # Insertar en bloque
        df.to_sql("diviplo", con=engine, if_exists="append", index=False, method="multi")

        return {"status": "ok", "mensaje": f"✅ Datos cargados correctamente: {len(df)} filas"}

    except Exception as e:
        print("🔥 ERROR REAL:", str(e))
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

@router.post("/reporte_eleciones")
async def reporte_eleciones(input: Request, token: str =  Depends(oauth2_scheme_2)):

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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#produccion 
    
        # ruta = "C:/Users/nicolas.valbuena/Documents/baken_dirop/"#ruta_absulota
        
        contents = await input.form()
        documento = reporte_eleciones_pdf(contents)

        # hechos_file = contents['hechos_file']
        # leer_resultados = input_json['leer_resultados']

        # print(hechos_file) 



        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()


        # await actualizar_datos()
        dato={
            "nombre":documento[1],
            "link":documento[0]
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
     config = uvicorn.Config("pazos_fronterizos:app", port=PUERTO+11, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





