from typing import Annotated, List
from __init__ import *
from fastapi import FastAPI, File, UploadFile, Form

router = APIRouter()

#importaciones a modulos propios

app = FastAPI(title="DIROP",
              description="api para el manejo de los resultados",
              version='1.0.1')

origins = [
"*",
]
import psycopg2
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

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
@router.post("/datos")
async def borrar_datos(input: Request, token: str =  Depends(oauth2_scheme_2)):
    
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

        input_json = await input.form()
        fecha_inicial = input_json['fecha_inicial']
        fecha_final = input_json['fecha_final']

        print(input_json)
        saludo = {
            'informacion':'datos no aliminados hay fechas vacias'
            }

        if fecha_inicial != '' and  fecha_final != '':
            
            eliminar_bd_posgrest(fecha_inicial, fecha_final)
            saludo = {
            'informacion':'datos eliminados'
            }

        return saludo




@router.post("/api")
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
        hechos_file =contents["hechos"]
        leer_resultados =contents["resultados"]
        # input_json:UploadFile = File(input)
        # print(input.receive)
        DIRECION = os.getenv('DIRECION')
        ruta = DIRECION
        dirercion_archvios = '{}cargar_datos_excel/documentos'.format(ruta)

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

        with open(getcwd() + "/documentos/HECHOS ARCHIVO PLANO.xlsx", "wb")as myfile:
            hechos = await hechos_file.read()
            myfile.write(hechos)
            myfile.close()

        with open(getcwd() + "/documentos/RESULTADOS APLICATIVO.xlsx", "wb")as myfile:
            resultados = await leer_resultados.read()
            myfile.write(resultados)
            myfile.close()

        # if leer_herradicacion.filename != "":
                
        #     with open(getcwd() + "/documentos/ERRADICACION APLICATIVO.xlsx", "wb")as myfile:
        #         resultados = await leer_herradicacion.read()
        #         myfile.write(resultados)
        #         myfile.close()

        print("---x---")
        await cargar_resultados()
        
        os.system('python actualizar.py')
        
        # Establecer conexión y ejecutar operaciones
        conn = connect()
        cursor = conn.cursor()

        # Insertar nueva actualización
        insert_query = '''
            INSERT INTO actulizacion_data (descripcion)
            VALUES ('Datos Actualizados');
        '''
        cursor.execute(insert_query)
        conn.commit()  # ✅ importante para que el INSERT se guarde

        # Obtener el último registro
        select_query = '''
            SELECT * FROM actulizacion_data 
            ORDER BY id DESC
            LIMIT 1;
        '''
        cursor.execute(select_query)
        ultimo_registro = cursor.fetchone()

        # Cerrar cursor y conexión
        cursor.close()
        conn.close()
        
        saludo = {
            'informacion':'Informacion Cargada en la base de Datos ',
            'fultimo_registro': ultimo_registro
        }
        # await actualizar_datos()
        return saludo

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
     config = uvicorn.Config("cargar_datos_excel:app", port=PUERTO+30, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





