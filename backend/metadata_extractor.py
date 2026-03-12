from sqlalchemy import create_engine, inspect
import pandas as pd
from config import DB_URI

engine = create_engine(DB_URI)

def extract_metadata():

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    metadata = []

    for table in tables:

        columns = inspector.get_columns(table)

        for column in columns:

            metadata.append({
                "table_name": table,
                "column_name": column["name"],
                "data_type": str(column["type"])
            })

    df = pd.DataFrame(metadata)

    return df