import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "USER": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASSWORD"),
    "HOST": os.getenv("DB_HOST"),
    "DATABASE": os.getenv("DB_DATABASE"),
}
