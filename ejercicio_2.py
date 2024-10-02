import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Configuración del diseño para que ocupe todo el ancho
st.set_page_config(layout="wide")

# Dividir la pantalla en tres columnas: enunciado, gráfico, e interpretación
col1, col2, col3 = st.columns([1, 2, 1])  # El gráfico será más grande que los textos

# Columna 1: Enunciado
with col1:
    st.write("""
    ### Descripción del Ejercicio 2
    Un sistema distribuido tiene 20 nodos. Cada nodo puede procesar \(x\) peticiones por segundo. 
    El sistema en su conjunto no puede procesar más de 400 peticiones por segundo debido a limitaciones de red. 
    El objetivo es maximizar el número de peticiones procesadas sin exceder la capacidad de la red.
    """)

# Parámetros de entrada
nodos = st.slider('Número de nodos', 1, 50, 20)
max_peticiones_sistema = st.slider('Límite máximo de peticiones del sistema', 100, 1000, 400)

# Función para calcular las peticiones procesadas por el sistema
def peticiones_procesadas_por_nodo(x):
    return nodos * x

# Valores de peticiones por nodo
x_val = np.linspace(1, 20, 100)  # Peticiones por nodo entre 1 y 20
peticiones_totales = peticiones_procesadas_por_nodo(x_val)

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Peticiones procesadas por el sistema')
    st.write('')
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño de gráfico original
    ax.plot(x_val, peticiones_totales, label='Peticiones procesadas', color='b')
    ax.axhline(max_peticiones_sistema, color='r', linestyle='--', label=f'Límite de {max_peticiones_sistema} peticiones')
    ax.set_title('Peticiones procesadas por el sistema vs Peticiones por nodo')
    ax.set_xlabel('Peticiones por nodo')
    ax.set_ylabel('Peticiones totales procesadas')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Peticiones por Nodo (x)**: El gráfico muestra cómo varía el número total de peticiones procesadas por el sistema a medida que cada nodo procesa más peticiones por segundo.
    - **Peticiones Totales**: Se observa que el número de peticiones totales aumenta con las peticiones procesadas por cada nodo hasta que se alcanza el límite máximo de peticiones del sistema.
    - **Conclusión**: Para maximizar las peticiones procesadas sin exceder la capacidad del sistema, el valor óptimo de peticiones por nodo debe ajustarse para no superar el límite de **{max_peticiones_sistema}** peticiones por segundo.
    """)

    # Mostrar el número de nodos y el límite máximo de peticiones del sistema
    st.write(f"**Número de nodos**: {nodos}")
    st.write(f"**Límite máximo de peticiones del sistema**: {max_peticiones_sistema} peticiones")
