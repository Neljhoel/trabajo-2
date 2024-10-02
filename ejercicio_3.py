import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Configuración del diseño para que ocupe todo el ancho
st.set_page_config(layout="wide")

# Dividir la pantalla en tres columnas: enunciado, gráfico, e interpretación
col1, col2, col3 = st.columns([1, 2, 1])

# Columna 1: Enunciado
with col1:
    st.write("""
    ### Descripción del Ejercicio 3
    Un script de Python tarda \(5x + 2\) segundos en procesar \(x\) datos. Por cada dato adicional, 
    el tiempo de ejecución crece linealmente. Sin embargo, el sistema tiene un límite de tiempo de ejecución de 50 segundos. 
    ¿Cuál es el número máximo de datos que puede procesar el script sin exceder el límite de tiempo?
    """)

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Tiempo de ejecución del script vs Número de datos procesados')
    st.write('')

    # Parámetro de entrada: límite de tiempo
    limite_tiempo = st.slider('Límite máximo de tiempo (segundos)', 10, 100, 50)

    # Función para calcular el tiempo de ejecución
    def tiempo_ejecucion(x):
        return 5 * x + 2

    # Valores de x (número de datos procesados)
    x_val = np.arange(0, 11)  # Número de datos procesados entre 0 y 10
    tiempos = tiempo_ejecucion(x_val)

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_val, tiempos, label='Tiempo de ejecución', color='b', marker='o')
    ax.axhline(limite_tiempo, color='r', linestyle='--', label=f'Límite de {limite_tiempo} segundos')
    ax.set_title('Tiempo de ejecución del script vs Número de datos procesados')
    ax.set_xlabel('Número de datos procesados')
    ax.set_ylabel('Tiempo de ejecución (segundos)')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Número de Datos Procesados (x)**: El gráfico muestra cómo el tiempo de ejecución del script aumenta con el número de datos procesados.
    - **Tiempo de Ejecución**: El tiempo de ejecución crece linealmente a medida que se procesan más datos, a razón de \(5\) segundos por dato más un tiempo base de 2 segundos.
    - **Conclusión**: El número máximo de datos que el script puede procesar sin exceder el límite de tiempo es aquel para el cual el tiempo de ejecución no sobrepasa el límite de **{limite_tiempo}** segundos.
    """)

    # Mostrar el límite de tiempo
    st.write(f"**Límite de tiempo**: {limite_tiempo} segundos")
