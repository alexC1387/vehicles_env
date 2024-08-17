import streamlit as st
import pandas as pd
import plotly.express as px

#Encabezado
st.header("Estadisticas de vehículos vendidos")
# Leer el archivo CSV en un DataFrame
df = pd.read_csv('vehicles_us.csv')
print(df.head())

    
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión') # crear un botón 2
       
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
           
    # crear un histograma
    fig = px.histogram(df, x="odometer")
       
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')


    fig = px.scatter(df, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)  
