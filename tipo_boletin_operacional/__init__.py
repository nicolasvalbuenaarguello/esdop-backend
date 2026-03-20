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


from a_a_guardar_evento.models.modelsUser import ModelUser
from a_a_guardar_evento.models.conexion_mysql import *
from a_a_guardar_evento.models.ingresar_user_db import *


import sys
from pathlib import Path

IP_SEGURITY = os.getenv('IP_SEGURITY')
SECRETE_KEY = os.getenv('SECRETE')
ALGORITHM = os.getenv('ALGORITHM')