import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.header('Dashboard de anúncios de carros')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma do preço dos carros')
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Relação entre preço e quilometragem')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
