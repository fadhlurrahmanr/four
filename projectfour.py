import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Project Four")
st.write("## Mini Dashboard SDGs")

df = pd.read_csv('data/inclusive.csv', sep = ';')

st.write("### 5 Data Pertama")
st.write(df.head() )

st.write("### 5 Data Terakhir")
st.write(df.tail() )


#fadel



#Arina



#Fijar


#Nindya

