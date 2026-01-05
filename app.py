import streamlit as st
import pandas as pd

st.set_page_config(page_title="Earnings Manipulator App")

st.title("📊 Earnings Manipulator Dataset")

@st.cache_data
def load_data():
    return pd.read_excel("Earnings Manipulator (1).xlsx")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Dataset Shape")
st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.subheader("Column Analysis")
column = st.selectbox("Choose a column", df.columns)
st.write(df[column].describe())
