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
    ### Descripción del Ejercicio 1
    Un algoritmo necesita procesar datos en lotes. Cada lote requiere \(x\) MB de memoria, 
    pero la capacidad total de memoria disponible es de 1024 MB. 
    El algoritmo puede procesar un máximo de 8 lotes. El objetivo es maximizar la cantidad de datos procesados, 
    pero cada lote más allá del quinto reduce su eficiencia en un 20%.
    """)

# Parámetros del problema
memoria = 1024  # MB de memoria disponible
lotes_ma = 8  # Número máximo de lotes
eficiencia_re = 0.8  # Eficiencia reducida para lotes más allá del quinto

# Función para calcular la cantidad de datos procesados
def datos_procesados(n, x):
    if n <= 5:
        return n * x
    else:
        return 5 * x + (n - 5) * eficiencia_re * x

# Entrada del número máximo de lotes en la interfaz
max_lotes_input = st.slider('Número máximo de lotes', 1, 10, 8)

# Cálculo de datos procesados y memoria usada por lote
lotes = np.arange(1, max_lotes_input + 1)
memorias = memoria / lotes  
datos = np.array([datos_procesados(n, memoria / n) for n in lotes])

# Columna 2: Gráfico
with col2:
    st.subheader("Resultados Gráficos")

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(lotes, datos, marker='o', linestyle='-', color='b', label='Datos procesados')
    ax.set_title('Cantidad de datos procesados vs Número de lotes')
    ax.set_xlabel('Número de lotes')
    ax.set_ylabel('Datos procesados (MB)')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Número de Lotes (x)**: El gráfico muestra cómo varía la cantidad de datos procesados en función del número de lotes procesados.
    - **Datos Procesados**: Se observa que la cantidad de datos procesados aumenta al incrementar el número de lotes hasta el quinto lote.
    - **Eficiencia Reducida**: Después de procesar 5 lotes, la eficiencia del procesamiento disminuye un 20% para cada lote adicional, lo cual está reflejado en la pendiente más baja del gráfico.
    - **Conclusión**: Para maximizar la cantidad de datos procesados, se recomienda procesar 5 lotes, ya que más allá de este número la eficiencia disminuye.
    """)

    # Mostrar el número máximo de lotes que se puede procesar eficientemente
    st.write(f"**Límite máximo de lotes**: {max_lotes_input}")
