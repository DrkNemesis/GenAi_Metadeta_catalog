from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_business_metadata(table, column, datatype):

    prompt = f"""
You are a data catalog assistant.

Generate a business term and description for the following database column.

Table: {table}
Column: {column}
Data Type: {datatype}

Return in this format:

Business Term:
Description:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content