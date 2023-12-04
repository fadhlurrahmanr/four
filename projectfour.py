import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Project Four")

st.write("## Mini Dashboard SDGs Indonesia")

st.write("#### Kelompok Four")
st.markdown("Anggota Kelompok: Arina, Fadhlurrahman, Fijar, Nindya") 

df = pd.read_csv('data/inclusive.csv', sep = ',')

st.write("##### 1. Statistik Seluruh Provinsi per Tahun")

tahun3 = st.selectbox(
    "Pilih Tahun",
    options = df["year"].unique() )

df3 = df.query(
    'year == @tahun3' )

attributes = st.multiselect(
    "Pilih Indikator SDGs :",
    options = ['PDRB per Orang yang Bekerja', 'PDRB per Kapita', 'Keluhan Kesehatan per Bulan (Persen)', 'Keterbukaan Perdagangan', 'Sektor Formal', 'Pengangguran (Persen)', 'Indeks Pembangunan Manusia', 'Belanja Pemerintah', 'Belanja Modal Pemerintah', 'Kemiskinan (Persen)', 'Rasio Gini', 'Sanitasi yang Layak', 'Air Bersih', 'Tingkat Kelulusan Sekolah (SMA)', 'Pertanian', 'Angka Harapan Hidup', 'PDRB Nominal', 'Populasi (ribuan)', 'Investasi Sektor Swastan', 'PMA', 'PMDN'],
    default=['PDRB per Kapita'] )

plot_bar = px.bar(df3,
                  x = df["province"].unique(),
                  y = attributes,
                 title = "Grafik Bar")

plot_bar.update_layout(
    xaxis_title = 'Provinsi' )

st.plotly_chart(plot_bar)


st.write("##### 2. Statistik per Provinsi")

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

attributes2 = st.multiselect(
    "Pilih Indikator SDGs untuk ditampilkan menjadi Grafik:",
    options=['PDRB per Orang yang Bekerja', 'PDRB per Kapita', 'Keluhan Kesehatan per Bulan (Persen)', 'Keterbukaan Perdagangan', 'Sektor Formal', 'Pengangguran (Persen)', 'Indeks Pembangunan Manusia', 'Belanja Pemerintah', 'Belanja Modal Pemerintah', 'Kemiskinan (Persen)', 'Rasio Gini', 'Sanitasi yang Layak', 'Air Bersih', 'Tingkat Kelulusan Sekolah (SMA)', 'Pertanian', 'Angka Harapan Hidup', 'PDRB Nominal', 'Populasi (ribuan)', 'Investasi Sektor Swastan', 'PMA', 'PMDN'],
    default=['PDRB per Kapita'] )

plot_grafik = px.line(
    df2,
    x = "year", y= attributes2, 
    title = "Grafik" )

st.plotly_chart(plot_grafik)

