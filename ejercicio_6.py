import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuración del diseño para que ocupe todo el ancho
st.set_page_config(layout="wide")

# Dividir la pantalla en tres columnas: enunciado, gráfico, e interpretación
col1, col2, col3 = st.columns([1, 2, 1])

# Columna 1: Enunciado
with col1:
    st.write("""
    ### Descripción del Ejercicio 6
    Un sistema de transmisión de datos tiene un ancho de banda total de 1000 Mbps. Cada archivo que se transmite utiliza \(x\) Mbps. 
    El sistema puede transmitir un máximo de 50 archivos a la vez, y cada archivo adicional más allá de 30 reduce el ancho de banda disponible en un 5%. 
    El objetivo es maximizar el número de archivos transmitidos sin exceder el ancho de banda disponible.
    """)

# Función para calcular el ancho de banda disponible
def calcular_ancho_banda(archivos_transmitidos, ancho_banda_total=1000):
    if archivos_transmitidos > 30:
        archivos_extra = archivos_transmitidos - 30
        reduccion = (5 / 100) * archivos_extra
        ancho_banda_disponible = ancho_banda_total * (1 - reduccion)
    else:
        ancho_banda_disponible = ancho_banda_total
    
    return max(0, ancho_banda_disponible)

# Función para maximizar el número de archivos transmitidos
def maximizar_archivos(x, ancho_banda_total=1000):
    for archivos in range(50, 0, -1):  
        ancho_banda_disponible = calcular_ancho_banda(archivos, ancho_banda_total)
        if archivos * x <= ancho_banda_disponible:  
            return archivos, ancho_banda_disponible
    return 0, 0

# Parámetro de entrada: ancho de banda por archivo y ancho de banda total
x = st.slider("Ancho de banda por archivo (Mbps)", min_value=1, max_value=100, value=20)
ancho_banda_total = st.slider("Ancho de banda total del sistema (Mbps)", min_value=500, max_value=2000, value=1000)

# Definir valores por defecto antes del botón
archivos_max, ancho_banda_restante = 0, 0

# Columna 2: Gráfico (sin modificaciones)
with col2:
    st.title("Maximización de Transmisión de Archivos con Gráfico")
    
    # Cálculo de archivos máximos y ancho de banda restante solo si se presiona el botón
    if st.button("Calcular Máximo de Archivos"):
        archivos_max, ancho_banda_restante = maximizar_archivos(x, ancho_banda_total)
        st.write(f"Número máximo de archivos que se pueden transmitir: {archivos_max}")
        st.write(f"Ancho de banda disponible restante: {ancho_banda_restante:.2f} Mbps")

        # Gráfico
        archivos = np.arange(1, 51)
        ancho_banda_disponible = [calcular_ancho_banda(a, ancho_banda_total) for a in archivos]
        fig, ax = plt.subplots(figsize=(10, 6))  # Mantengo el tamaño original
        ax.plot(archivos, ancho_banda_disponible, label='Ancho de banda disponible (Mbps)')
        ax.axvline(x=30, color='red', linestyle='--', label='Límite sin penalización')
        ax.axvline(x=archivos_max, color='green', linestyle='--', label=f'Máximo Archivos: {archivos_max}')
        ax.set_xlabel('Número de archivos transmitidos')
        ax.set_ylabel('Ancho de banda disponible (Mbps)')
        ax.set_title('Relación entre número de archivos y ancho de banda disponible')
        ax.legend()
        st.pyplot(fig)

# Columna 3: Interpretación
with col3:
    st.write("""
    ### Interpretación del Gráfico
    - **Número de Archivos Transmitidos (x)**: El gráfico muestra cómo varía el ancho de banda disponible a medida que se transmiten más archivos.
    - **Ancho de Banda Disponible**: El ancho de banda total es de 1000 Mbps, pero a medida que se transmiten más de 30 archivos, el ancho de banda disponible disminuye debido a una penalización del 5% por archivo adicional.
    - **Conclusión**: Para maximizar el número de archivos transmitidos sin exceder el ancho de banda disponible, el valor óptimo es **{archivos_max}** archivos. El ancho de banda disponible restante es de **{ancho_banda_restante:.2f} Mbps**.
    """)
