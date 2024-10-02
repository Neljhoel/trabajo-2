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
    ### Descripción del Ejercicio 8
    El entrenamiento de un modelo de deep learning en una GPU consume \(x\) unidades de energía por lote. El objetivo es maximizar el tamaño del lote \(x\), 
    pero el consumo de energía total no puede exceder las **200 unidades**. Cada lote adicional más allá de 10 reduce el rendimiento en un **10%**.
    """)

# Función para calcular el consumo de energía
def energia_consumida(x):
    if x <= 10:
        return x
    else:
        return x * (1 + 0.1 * (x - 10))

# Función para calcular el consumo total de energía
def consumo_total(x):
    return x * energia_consumida(x)

# Parámetro de entrada: tamaño del lote
tamaño_lote = st.slider('Selecciona el tamaño del lote (x)', min_value=1, max_value=20, value=10)

# Cálculo de valores
x_values = np.linspace(1, 20, 100)
consumo = np.array([consumo_total(x) for x in x_values])
x_max = np.max(x_values[consumo <= 200])  # Tamaño de lote máximo que satisface la restricción de 200 unidades

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Consumo Total de Energía vs Tamaño de Lote')

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_values, consumo, label='Consumo total de energía', color='b')
    ax.axhline(y=200, color='r', linestyle='--', label='Restricción de 200 unidades de energía')
    ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
    ax.plot(x_max, consumo_total(x_max), 'go')
    ax.axvline(x=tamaño_lote, color='purple', linestyle='--', label=f'Tamaño de lote seleccionado: {tamaño_lote}')
    ax.plot(tamaño_lote, consumo_total(tamaño_lote), 'mo')
    ax.set_title('Consumo total de energía vs Tamaño de lote')
    ax.set_xlabel('Tamaño de lote (x)')
    ax.set_ylabel('Consumo total de energía (unidades)')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Tamaño de Lote (x)**: El gráfico muestra cómo varía el consumo total de energía a medida que cambia el tamaño del lote.
    - **Consumo Total de Energía**: Para tamaños de lote menores o iguales a 10, el consumo de energía por lote es proporcional a su tamaño. A partir de 10, cada lote adicional reduce la eficiencia del sistema en un **10%**, lo que resulta en un incremento no lineal del consumo de energía.
    - **Conclusión**: El tamaño de lote máximo que satisface la restricción de **200 unidades de energía** es aproximadamente \(x = {x_max:.2f}\). Para el tamaño de lote seleccionado \(x = {tamaño_lote}\), el consumo total de energía es de **{consumo_total(tamaño_lote):.2f}** unidades.
    """)

    # Mostrar el tamaño de lote máximo y el consumo para el tamaño seleccionado
    st.write(f"**Tamaño de lote máximo que satisface la restricción**: {x_max:.2f}")
    st.write(f"**Consumo total de energía para el tamaño de lote seleccionado ({tamaño_lote})**: {consumo_total(tamaño_lote):.2f} unidades")
