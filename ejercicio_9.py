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
    ### Descripción del Ejercicio 9
    Una empresa almacena datos en la nube. El costo de almacenamiento por TB es de:

    \[
    C(x) = 50 + 5x
    \]

    donde \(x\) es la cantidad de TB de almacenamiento utilizado. La empresa tiene un presupuesto de **500 dólares**.
    El objetivo es maximizar la cantidad de datos almacenados sin exceder el presupuesto.
    """)

# Función para calcular el costo de almacenamiento
def costo_almacenamiento(x):
    return 50 + 5 * x

# Presupuesto y cantidad de almacenamiento
presupuesto = 500
x_val = np.linspace(0, 100, 100)
costos = costo_almacenamiento(x_val)
x_max = (presupuesto - 50) / 5  # Cantidad máxima de TB que se puede almacenar sin exceder el presupuesto

# Parámetro de entrada: cantidad de almacenamiento
cantidad_almacenamiento = st.slider(
    'Selecciona la cantidad de almacenamiento (TB)',
    min_value=0,
    max_value=100,
    value=0
)

# Cálculo del costo para el almacenamiento seleccionado
costo_seleccionado = costo_almacenamiento(cantidad_almacenamiento)

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title('Costo de Almacenamiento vs Cantidad de TB')

    # Creación del gráfico
    fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
    ax.plot(x_val, costos, label='Costo de almacenamiento', color='b')
    ax.axhline(y=presupuesto, color='r', linestyle='--', label='Presupuesto de 500 dólares')
    ax.axvline(x=x_max, color='g', linestyle='--', label=f'Máximo en x={x_max:.2f}')
    ax.plot(cantidad_almacenamiento, costo_seleccionado, 'go', label='Seleccionado')
    ax.set_title('Costo de Almacenamiento vs Cantidad de TB')
    ax.set_xlabel('Cantidad de almacenamiento (TB)')
    ax.set_ylabel('Costo de almacenamiento (dólares)')
    ax.grid(True)
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Cantidad de Almacenamiento (TB)**: El gráfico muestra cómo el costo de almacenamiento aumenta de manera lineal con respecto a la cantidad de TB almacenados.
    - **Presupuesto de 500 dólares**: La empresa tiene un presupuesto límite de **500 dólares**. Esto implica que el almacenamiento máximo que puede permitirse es de **{x_max:.2f} TB**.
    - **Conclusión**: Para almacenar una cantidad de **{cantidad_almacenamiento} TB**, el costo de almacenamiento es de **{costo_seleccionado:.2f} dólares**. Si se desea maximizar el almacenamiento sin exceder el presupuesto, la cantidad máxima es de **{x_max:.2f} TB**.
    """)

    # Mostrar el costo de almacenamiento y el almacenamiento máximo dentro del presupuesto
    st.write(f"**Cantidad máxima de almacenamiento que satisface el presupuesto**: {x_max:.2f} TB")
    st.write(f"**Costo de almacenamiento para {cantidad_almacenamiento} TB**: {costo_seleccionado:.2f} dólares")
