from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from datetime import datetime, timedelta
from typing import Dict
import os
from dotenv import load_dotenv

from models.conexion_mysql import Databa_bases_2
from models.entities.user import User
from models.modelsUser import ModelUser

# Carga de variables de entorno
load_dotenv()

# Configuración JWT
SECRETE_KEY = "db9b50e619be3e9b6dcc8b0f75e8be4155ae87f706170b5032b0de347052056a"
ALGORITHM = "HS256"

# OAuth2: token obligatorio para acceder
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/")

# Conexión única a la base de datos
db = Databa_bases_2.conexion_directa()

async def verificar_token(token: str = Depends(oauth2_scheme)) -> Dict:
    try:
        # Decodificar el token JWT
        token_decode = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        payload = jwt.decode(token, key=SECRETE_KEY, algorithms=[ALGORITHM])
        user_name = payload.get("sub")
        code = payload.get("code")
        exp = payload.get("exp")

        # Verificación básica del contenido
        if not user_name or not exp:
            raise HTTPException(status_code=401, detail="Token incompleto o inválido.")

        # Verificar expiración con margen de seguridad
        tiempo_exp = datetime.utcfromtimestamp(exp)
        if datetime.utcnow() > tiempo_exp - timedelta(minutes=10):
            raise HTTPException(status_code=401, detail="Sesión expirada.")

        # Validación en base de datos
        user = User(user_name=user_name)
        logged_user = ModelUser.loguin(db, user)

        if not logged_user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado.")
        
        if getattr(logged_user, "disabled", False):
            raise HTTPException(status_code=403, detail="Usuario deshabilitado.")

        # Retornar información útil para los endpoints
   
        return {
            "user_name": user_name,
            "code": code,
            "exp": exp,
            "user_obj": logged_user
        }

    except ExpiredSignatureError:
        print("--")
        raise HTTPException(status_code=401, detail="Token expirado.")
    except JWTError:
        print("-/-")
        raise HTTPException(status_code=401, detail="Token inválido.")
    except Exception as e:
        print(f"[verificar_token] ❌ Error inesperado: {e}")
        raise HTTPException(status_code=500, detail="Error interno de autenticación.")
