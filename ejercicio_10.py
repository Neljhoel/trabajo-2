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
    ### Descripción del Ejercicio 10
    Un sistema de mensajería tiene una latencia \(L(x)\) definida como:

    \[
    L(x) = 100 - 2x
    \]

    donde \(x\) es el número de mensajes enviados por segundo. La latencia no puede ser inferior a **20 ms** debido a restricciones del protocolo. 
    El objetivo es maximizar el número de mensajes enviados sin que la latencia caiga por debajo de este límite.
    """)

# Función para calcular la latencia
def latencia(x):
    return 100 - 2 * x

# Parámetro de entrada: número de mensajes por segundo
x_val = np.linspace(0, 60, 100)
latencias = latencia(x_val)
x_max = 40  # Número máximo de mensajes sin que la latencia baje de 20 ms

# Parámetro de entrada: número de mensajes por segundo seleccionado por el usuario
numero_mensajes = st.slider(
    'Selecciona el número de mensajes por segundo',
    min_value=0,
    max_value=60,
    value=0
)

# Cálculo de la latencia seleccionada
latencia_seleccionada = latencia(numero_mensajes)

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Latencia vs Número de Mensajes')

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_val, latencias, label='Latencia (ms)', color='b')
    ax.axhline(y=20, color='r', linestyle='--', label='Latencia mínima de 20 ms')
    ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max}')
    ax.plot(numero_mensajes, latencia_seleccionada, 'go', label='Seleccionado')
    ax.set_title('Latencia vs Número de Mensajes')
    ax.set_xlabel('Número de mensajes por segundo')
    ax.set_ylabel('Latencia (ms)')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Número de Mensajes por Segundo (x)**: El gráfico muestra cómo la latencia disminuye a medida que aumenta el número de mensajes enviados por segundo.
    - **Latencia Mínima**: La latencia no puede caer por debajo de **20 ms** debido a restricciones del protocolo. Esto establece un límite en el número de mensajes que se pueden enviar sin reducir la latencia por debajo de este valor.
    - **Conclusión**: El número máximo de mensajes que se pueden enviar sin que la latencia caiga por debajo de **20 ms** es aproximadamente \(x = {x_max}\). Para \(x = {numero_mensajes}\), la latencia es de **{latencia_seleccionada:.2f} ms**.
    """)

    # Mostrar la latencia para el número seleccionado de mensajes
    st.write(f"**Número máximo de mensajes por segundo**: {x_max}")
    st.write(f"**Latencia para {numero_mensajes} mensajes por segundo**: {latencia_seleccionada:.2f} ms")
