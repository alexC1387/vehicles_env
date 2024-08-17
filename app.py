import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("Estadísticas de vehículos vendidos")

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('vehicles_us.csv')

# Limpiar el DataFrame
for col in df.columns:
    if df[col].dtype == 'object':
        # Rellenar valores NaN con una cadena vacía
        df[col].fillna('', inplace=True)
    else:
        # Rellenar valores NaN con 0 y convertir a float
        df[col].fillna(0, inplace=True)
        df[col] = df[col].astype(float)

# Mostrar el DataFrame en la aplicación Streamlit
st.write(df)

# Botones para construir gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)