import streamlit as st
import pandas as pd
import plotly.express as px

#Encabezado
st.header("Estadisticas de vehículos vendidos")
# Leer el archivo CSV en un DataFrame
df = pd.read_csv('vehicles_us.csv')

# Limpiar datos
df = df.replace({pd.NA: None, '': None})
df['price'] = pd.to_numeric(car_data['price'], errors='coerce')
df['odometer'] = pd.to_numeric(car_data['odometer'], errors='coerce')
df.columns = df.columns.str.strip()

# Muestra el DataFrame en la aplicación Streamlit
st.write(df)
        
df = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión') # crear un botón 2
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)       