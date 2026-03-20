from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, File, Form, UploadFile, Request
from pydantic import BaseModel
from datetime import datetime
from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()
import zipfile