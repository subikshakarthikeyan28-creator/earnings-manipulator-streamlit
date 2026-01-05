import streamlit as st
import pandas as pd

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Earnings Manipulator Dataset",
    layout="wide"
)

# -------------------------------------------------
# App Title
# -------------------------------------------------
st.title("📊 Earnings Manipulator Dataset")

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_excel("earnings_data.xlsx")

df = load_data()

# -------------------------------------------------
# Dataset Preview
# -------------------------------------------------
st.subheader("Dataset Preview")
st.dataframe(df)

# -------------------------------------------------
# Dataset Shape
# -------------------------------------------------
st.subheader("Dataset Shape")
st.write(f"**Rows:** {df.shape[0]}")
st.write(f"**Columns:** {df.shape[1]}")

# -------------------------------------------------
# Column Analysis
# -------------------------------------------------
st.subheader("Column Analysis")

column = st.selectbox(
    "Choose a column",
    df.columns
)

st.write(df[column].describe())


