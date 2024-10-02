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
    ### Descripción del Ejercicio 4
    Un servidor web procesa \(x\) peticiones por segundo, y el uso de CPU sigue la fórmula \(2x^2 + 10x\). 
    La CPU no puede exceder el 80% de uso. El objetivo es minimizar el uso de la CPU sin caer por debajo del umbral de 10 peticiones por segundo.
    """)

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Uso de CPU vs Número de peticiones procesadas por segundo')
    st.write('')

    # Parámetro de entrada: límite de uso de CPU y máximo de peticiones
    limite_uso_cpu = st.slider('Límite máximo de uso de CPU (%)', 50, 100, 80)
    max_peticiones = st.slider('Máximo de peticiones procesadas por segundo', 5, 50, 20)

    # Función para calcular el uso de CPU
    def uso_cpu(x):
        return 2 * x**2 + 10 * x

    # Valores de x (número de peticiones por segundo)
    x_val = np.arange(0, max_peticiones + 1, 0.1)
    uso_cpu_values = uso_cpu(x_val)

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_val, uso_cpu_values, label='Uso de CPU', color='b')
    ax.axhline(limite_uso_cpu, color='r', linestyle='--', label=f'Límite del {limite_uso_cpu}% de CPU')
    ax.set_title('Uso de CPU vs Número de peticiones procesadas por segundo')
    ax.set_xlabel('Número de peticiones procesadas por segundo')
    ax.set_ylabel('Uso de CPU (%)')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Número de Peticiones por Segundo (x)**: El gráfico muestra cómo el uso de CPU crece de manera no lineal a medida que el número de peticiones procesadas por segundo aumenta.
    - **Uso de CPU**: El uso de CPU sigue una relación cuadrática con el número de peticiones por segundo, aumentando más rápidamente a medida que se procesan más peticiones.
    - **Conclusión**: El número máximo de peticiones procesadas por segundo sin exceder el límite de **{limite_uso_cpu}%** de uso de CPU debe ajustarse para mantenerse dentro de la capacidad del sistema.
    """)

    # Mostrar el límite de uso de CPU
    st.write(f"**Límite máximo de uso de CPU**: {limite_uso_cpu}%")
    st.write(f"**Máximo de peticiones procesadas por segundo**: {max_peticiones}")
