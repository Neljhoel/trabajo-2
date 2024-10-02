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
    ### Descripción del Ejercicio 7
    Un sistema de colas procesa \(x\) trabajos por segundo. La función del tiempo de respuesta \(T(x)\) es:

    \[
    T(x) = \frac{100}{x} + 2x
    \]

    El objetivo es minimizar el tiempo de respuesta del sistema, considerando que el sistema debe procesar al menos 5 trabajos por segundo.
    """)

# Función para calcular el tiempo de respuesta
def tiempo_respuesta(x):
    return (100 / x) + 2 * x

# Parámetro de entrada: número máximo de trabajos por segundo
max_x = st.slider('Selecciona el número de trabajos procesados por segundo', 5, 20, 20)

# Cálculo de valores
x_val = np.arange(5, max_x, 0.1)
tiempos = tiempo_respuesta(x_val)
x_optimo = np.sqrt(50)  # Valor óptimo calculado (mínimo de la función)
t_optimo = tiempo_respuesta(x_optimo)

# Columna 2: Gráfico
with col2:
    st.title('Tiempo de respuesta vs Número de trabajos procesados')
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_val, tiempos, label='Tiempo de respuesta', color='b')
    ax.axvline(x_optimo, color='r', linestyle='--', label=f'Mínimo en x={x_optimo:.2f}')
    ax.scatter(x_optimo, t_optimo, color='r', zorder=5)
    ax.set_title('Tiempo de respuesta vs Número de trabajos procesados')
    ax.set_xlabel('Número de trabajos por segundo')
    ax.set_ylabel('Tiempo de respuesta')
    ax.grid(True)
    ax.legend()
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Número de Trabajos Procesados por Segundo (x)**: El gráfico muestra cómo varía el tiempo de respuesta en función del número de trabajos procesados por segundo.
    - **Tiempo de Respuesta**: El tiempo de respuesta disminuye a medida que se incrementa el número de trabajos procesados por segundo, hasta alcanzar un punto mínimo. Después de ese punto, el tiempo de respuesta comienza a aumentar nuevamente.
    - **Conclusión**: El número óptimo de trabajos por segundo que minimiza el tiempo de respuesta es \(x = {x_optimo:.2f}\), con un tiempo de respuesta de \(T(x) = {t_optimo:.2f}\). Si se procesan más trabajos por segundo, el tiempo de respuesta comienza a aumentar.
    """)

    # Mostrar el número óptimo de trabajos procesados y el tiempo mínimo de respuesta
    st.write(f"**Número óptimo de trabajos por segundo**: {x_optimo:.2f}")
    st.write(f"**Tiempo mínimo de respuesta**: {t_optimo:.2f} segundos")
