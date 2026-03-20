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

    token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
    print(token_decode.get("exp"))

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
         
    #con esta variable se cambia el link de los documentos en pdf, se debe cambiar de acuerdo al entrono que se encuentre
    # link = "C:/inetpub/wwwroot/pagina_de_dirop/dociments/boletin/"#producci

        contents = await datos.form()
        #archivos
        boletin_fisico =contents["boletin_fisico"]
        radiograma_unidad =contents["radiograma_unidad"]
        denuncia_evento =contents["denuncia_evento"]
        informe_pdf =contents["informe_pdf"]


        #nombre de los archivos
        if boletin_fisico != "---":
            boletin_fisico_name =contents["boletin_fisico"].filename
            boletin = boletin_fisico_name
        else:
            boletin ="falta"

        if radiograma_unidad != "---":
            radiograma_unidad_name =contents["radiograma_unidad"].filename
            radiograma = radiograma_unidad_name
        else:
            radiograma="falta"
                
        if denuncia_evento != "---":
            denuncia_evento_name =contents["denuncia_evento"].filename
            denuncia = denuncia_evento_name
        else:
            denuncia = "falta"
                
        if informe_pdf != "---":
            informe_pdf_name =contents["informe_pdf"].filename
            informe = informe_pdf_name
        else:
            informe = "falta"

        # comprecion de archivos 
        documento_inf  = guardar_evento(contents, boletin, radiograma, denuncia, informe)

        print(documento_inf[0])
        print(documento_inf[4])

        if documento_inf[0] != "falta":
            with open(documento_inf[4]+str(documento_inf[0]), "wb")as myfile:
                boltin_f = await boletin_fisico.read()
                myfile.write(boltin_f)
                myfile.close()

        if documento_inf[1] != "falta":
            with open(documento_inf[4]+str(documento_inf[1]), "wb")as myfile:
                boltin_f = await radiograma_unidad.read()
                myfile.write(boltin_f)
                myfile.close()

        if documento_inf[2] != "falta":
            with open(documento_inf[4]+str(documento_inf[2]), "wb")as myfile:
                boltin_f = await denuncia_evento.read()
                myfile.write(boltin_f)
                myfile.close()
                
        if documento_inf[3] != "falta":
            with open(documento_inf[4]+str(documento_inf[3]), "wb")as myfile:
                boltin_f = await informe_pdf.read()
                myfile.write(boltin_f)
                myfile.close()

        dato={
            "respuesta":"vento Guardado con Exito",
            "eventos":documento_inf[5]
        }

        # print("guardar evento")
        return dato
app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))
print("guardar evento")
if __name__ == "__main__":
     config = uvicorn.Config("a_a_guardar_evento:app", port=PUERTO+31, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()

