import streamlit as st
import pandas as pd
import plotly.express as px

st.write("""
# Project Four

## Mini Dashboard SDGs Indonesia

""")

df = pd.read_csv('data/inclusive.csv', sep = ',')

st.write("## 1. Statistik per Provinsi")

provinsi = st.selectbox(
    "Pilih Provinsi", df["province"].unique() )
