from dotenv import load_dotenv
import os
from .settings import *


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
