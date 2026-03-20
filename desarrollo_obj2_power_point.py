from __init__ import *
from tipo_docker.k_c_boletin_comparativo_power_point.models.descarga_resultados.boltin_coe import *

router = APIRouter()

import os
import shutil

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

@router.post("/")
async def descarga(datos: Request, token: str =  Depends(oauth2_scheme_2)):
    
    #try:

        #token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        

        #user_name =  token_decode.get("sub")
        #exp = token_decode.get("exp")
        #code =  token_decode.get("code")
        #tiempo = datetime.utcfromtimestamp(exp)
        #tiempo_2 = tiempo-timedelta(minutes=10)
        #now = datetime.utcnow()+timedelta()
        #print(now)
        #if now > tiempo_2:
                #raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        #try:
            #token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
            #user_name =  token_decode.get("sub")
            #code =  token_decode.get("code")
            #exp = token_decode.get("exp")

            # tiempo = datetime.utcfromtimestamp(exp)


            #if user_name == None:
                #raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        #except JWTError:
            #raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
        #except JWTError.ExpiredSignatureError:
            #raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})
        
        #user = User(user_name = user_name )
        #logged_user = ModelUser.loguin(db, user)

        #if not logged_user:
            #raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})

        #if user.disabled:
            #raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
        #else:
        
            LINK = os.getenv('DIRECION_3_B')
            DIRECION = os.getenv('DIRECION')
            ruta = DIRECION
            link = LINK

            datos = await datos.form()

            link_2 = "C:/xampp/htdocs/JEMOP/dociments/mapa/"#desarrollo

            dato = compartivo_power_point(datos, link, ruta, 5000)
            return dato

    #except Exception as e:
        #print(e)
        #raise HTTPException(status_code=401, detail="su seccion expiro",headers={"WWW-Authenticate":"Bearer"})

app.include_router(router)

import uvicorn
IP = os.getenv('IP')
PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("desarrollo_obj2_power_point:app", port=PUERTO+167, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()