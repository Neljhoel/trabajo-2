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
    ### Descripción del Ejercicio 5
    Durante el entrenamiento de un modelo de machine learning, el **batch size** afecta el tiempo de entrenamiento. 
    La función que relaciona el tiempo de entrenamiento \(T(x)\) con el tamaño del lote \(x\) es:
    
    \[
    T(x) = \frac{1000}{x} + 0.1x
    \]
    
    El objetivo es minimizar el tiempo de entrenamiento. El tamaño del lote debe estar entre **16 y 128**.
    """)

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)')
    st.write('')

    # Parámetro de entrada: tamaño del lote
    batch_size = st.slider('Tamaño del lote', 16, 128, 16)  

    # Función para calcular el tiempo de entrenamiento
    def tiempo_entrenamiento(x):
        return (1000 / x) + 0.1 * x

    # Valores de x (batch size entre 16 y 128)
    x_val = np.arange(16, 129, 1)
    tiempos = tiempo_entrenamiento(x_val)
    min_index = np.argmin(tiempos)  # Índice del mínimo global
    batch_size_min = x_val[min_index]
    tiempo_min = tiempos[min_index]
    tiempo_actual = tiempo_entrenamiento(batch_size)

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_val, tiempos, label='Tiempo de entrenamiento', color='b')
    ax.axvline(x=batch_size_min, color='r', linestyle='--', label=f'Mínimo global en x={batch_size_min} (Tiempo: {tiempo_min:.2f})')
    ax.axvline(x=batch_size, color='g', linestyle='--', label=f'Tamaño de lote seleccionado: {batch_size} (Tiempo: {tiempo_actual:.2f})')

    ax.set_title('Tiempo de entrenamiento vs Tamaño del lote (Batch size)')
    ax.set_xlabel('Tamaño del lote (Batch size)')
    ax.set_ylabel('Tiempo de entrenamiento')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Tamaño del Lote (Batch size)**: El gráfico muestra cómo el tiempo de entrenamiento varía en función del tamaño del lote.
    - **Tiempo de Entrenamiento**: El tiempo de entrenamiento disminuye a medida que el tamaño del lote aumenta, pero crece nuevamente después de un punto mínimo.
    - **Conclusión**: El tamaño de lote que minimiza el tiempo de entrenamiento es **{batch_size_min}**, con un tiempo de **{tiempo_min:.2f}**. Para el tamaño de lote seleccionado de **{batch_size}**, el tiempo de entrenamiento es **{tiempo_actual:.2f}**.
    """)

    # Mostrar el tamaño de lote que minimiza el tiempo de entrenamiento y el tiempo para el tamaño seleccionado
    st.write(f"**Tamaño de lote óptimo**: {batch_size_min}")
    st.write(f"**Tiempo mínimo de entrenamiento**: {tiempo_min:.2f} segundos")
    st.write(f"**Tiempo de entrenamiento para el tamaño de lote seleccionado ({batch_size})**: {tiempo_actual:.2f} segundos")
