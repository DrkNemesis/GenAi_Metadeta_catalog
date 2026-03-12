import streamlit as st
import pandas as pd

from metadata_extractor import extract_metadata
from ai_generator import generate_business_metadata


st.title("AI Powered Data Catalog")

st.write("Metadata Catalog for DVD Rental Database")


if st.button("Load Metadata"):

    df = extract_metadata()

    st.success("Metadata Extracted")

    st.dataframe(df)


st.header("Generate Business Metadata")

table = st.text_input("Table Name")
column = st.text_input("Column Name")
datatype = st.text_input("Data Type")

if st.button("Generate Description"):

    result = generate_business_metadata(table, column, datatype)

    st.subheader("AI Generated Metadata")

    st.write(result)