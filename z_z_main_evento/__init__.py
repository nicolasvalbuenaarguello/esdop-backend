from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, File, Form, UploadFile, Request
from pydantic import BaseModel
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()