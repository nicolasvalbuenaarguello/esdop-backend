from datetime import timedelta, datetime
from __init__ import *
import time

import os
#print (os.getcwd())
IP_SEGURITY = os.getenv('IP_SEGURITY')
SECRETE_KEY = os.getenv('SECRETE')
ALGORITHM = os.getenv('ALGORITHM')
router = APIRouter()

#importaciones a modulos propios
oauth2_scheme = OAuth2PasswordBearer("/token")

app = FastAPI(title="SEJEC",
              description="api para el manejo de los resultados",
              version='1.0.2')

app.add_middleware(
    CORSMiddleware,
    allow_origins=IP_SEGURITY,
    allow_credentials=True,
    expose_headers=[],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_user_current(token: str =  Depends(oauth2_scheme)):
    try:

        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        user_name =  token_decode.get("sub")
        exp = token_decode.get("exp")

        tiempo = datetime.utcfromtimestamp(exp)
        now = datetime.utcnow()+timedelta()



        if user_name == None:
             raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    except JWTError:
        raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    
    
    user = User(user_name = user_name )
    # print(user_name)
    logged_user = ModelUser.loguin(user)


    if not logged_user:
         raise HTTPException(status_code=401, detail="no se puede verifcar credenciales",headers={"WWW-Authenticate":"Bearer"})
    return logged_user

def get_user_disable_current(user: User = Depends(get_user_current)):
     if user.disabled:
          raise HTTPException(status_code=400, detail="expiro credenciales",headers={"WWW-Authenticate":"Bearer"})
     else:
          raise HTTPException(status_code=200, detail="ejecutado con exito",headers={"WWW-Authenticate":"Bearer"})
     
@router.post("/token")
def login_token(formd_data: OAuth2PasswordRequestForm = Depends()):
        
        logged_user = Ingreso.logui(formd_data.username, formd_data.password)
        # info = {"error":datos}
        return logged_user

@router.post("/api")
# @router.post("/token")
async def loguin(datos: Request):
    
    datos = await datos.form()
    nonbre = datos['username']
    password = datos['password']
    
    datos = Ingreso.logui( nonbre, password)
    return datos

app.include_router(router)

import uvicorn
IP = os.getenv('IP')

PUERTO = int(os.getenv('PUERTO'))

if __name__ == "__main__":
     config = uvicorn.Config("loguin_app_serve_token_sejec:app", port=PUERTO+40, host = IP, log_level="info", reload=True)
     server = uvicorn.Server(config)
     server.run()





