import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URI = os.environ.get("DB_URI")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")