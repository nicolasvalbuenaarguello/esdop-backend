from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, File, Form, UploadFile, Request
from pydantic import BaseModel
from models.eliminar_posgrest_bd import *
from datetime import datetime
from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

from models.eliminar_posgrest_bd import *
import os

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, File, Form, UploadFile, Request
from jose import JWTError, jwt

from datetime import timedelta

from pydantic import BaseModel
from os import getcwd
import os
import shutil
from dotenv import load_dotenv

from models.entities.user import User
from models.modelsUser import ModelUser
from models.conexion_mysql import *
from models.ingresar_user_db import *
from models.guardar_evento import *


import sys
from pathlib import Path

IP_SEGURITY = os.getenv('IP_SEGURITY')
SECRETE_KEY = os.getenv('SECRETE')
ALGORITHM = os.getenv('ALGORITHM')
