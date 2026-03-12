import os
from dotenv import load_dotenv
load_dotenv()

DB_URI = "postgresql+psycopg2://postgres:root123@localhost:5432/pagila"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")