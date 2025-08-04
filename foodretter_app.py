import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurar página
st.set_page_config(page_title="Foodretter - Análisis de Datos", layout="centered")
st.title("Foodretter: Desperdicio Alimentario")

# -----------------------
# 1. Cargar los datos con pandas
# -----------------------
@st.cache_data
def cargar_datos():
    return pd.read_csv("desperdicio.csv")

df = cargar_datos()

# Mostrar la tabla completa
st.subheader("Datos")
st.dataframe(df)

# -----------------------
# 2. Función para graficar
# -----------------------
def graficar_por_nivel(nivel, color):
    df_filtrado = df[df["Nivel"] == nivel]  # Filtrar los datos por nivel
    fig, ax = plt.subplots()
    ax.bar(df_filtrado["Lugar"], df_filtrado["Toneladas"], color=color)
    ax.set_title(f"Desperdicio alimentario a nivel {nivel}")
    ax.set_ylabel("Toneladas")
    ax.set_xlabel("Categoría / Ciudad")
    st.pyplot(fig)

# -----------------------
# 3. Mostrar los gráficos por nivel
# -----------------------
niveles = df["Nivel"].unique()

for nivel in niveles:
    st.subheader(f"Nivel: {nivel}")
    color = "#66bb6a" if nivel == "Mundial" else "#42a5f5" if nivel == "Colombia" else "#ef5350"
    graficar_por_nivel(nivel, color)
