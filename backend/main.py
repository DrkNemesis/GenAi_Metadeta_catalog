from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from metadata_extractor import extract_metadata
from ai_generator import generate_business_metadata

app = FastAPI()

# allow React to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/metadata")
def get_metadata():
    data = extract_metadata()
    return data.to_dict(orient="records")


@app.post("/generate-description")
def generate_description(data: dict):

    table = data["table"]
    column = data["column"]
    datatype = data["datatype"]

    result = generate_business_metadata(table, column, datatype)

    return {"description": result}