import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Project Four")

st.write("## Mini Dashboard SDGs Indonesia")

st.write("#### Kelompok Four")
st.markdown("Anggota Kelompok: Arina, Fadhlurrahman, Fijar, Nindya") 

df = pd.read_csv('data/inclusive.csv', sep = ',')

st.write("##### 1. Statistik per Provinsi")

provinsi = st.selectbox(
    "Pilih Provinsi", df["province"].unique() )

tahun = st.multiselect(
    "Pilih tahun",
    options = df["year"].unique(),
    default = df["year"].unique() )

df2 = df.query(
    'province == @provinsi & year == @tahun'
)

st.dataframe(df2)