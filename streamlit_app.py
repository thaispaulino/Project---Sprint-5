import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px
import nbformat
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import os

# Certifique-se de que o arquivo vehicles.csv está no mesmo diretório
df = pd.read_csv('vehicles.csv')

st.header('Dados de anúncios de vendas de carros')

# Create a button
hist_button = st.button('Criar histograma')

# if the button is clicked
if hist_button:
  st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

  # create a histogram
  fig = px.histogram(df, x="odometer")

  # display the chart
  st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Criar um histograma para a coluna odometer')
if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para a coluna odometer')
  fig = px.histogram(df, x="odometer")
  st.plotly_chart(fig, use_container_width=True)

st.header('Model year vs Price')

st.write('Ainda não é um aplicativo funcional. Em construção.')
