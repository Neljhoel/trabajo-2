import streamlit as st
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value
import pandas as pd

# Configuración de la página de Streamlit
st.title("Maximización de NPV para Proyectos de R&D")
st.write("Este es un modelo de optimización binaria para seleccionar proyectos que maximicen el NPV, respetando restricciones de presupuesto anual.")

# Definir los parámetros
npv = [141, 187, 163, 155, 189, 127]  # NPV de cada proyecto
costs = [
    [75, 90, 80, 20, 100, 50],  # Año 1
    [25, 50, 60, 10, 32, 20],   # Año 2
    [20, 25, 25, 10, 10, 10],   # Año 3
    [15, 15, 15, 8, 10, 10],    # Año 4
    [10, 10, 15, 5, 8, 5]       # Año 5
]
budgets = [250, 75, 50, 50, 50]  # Presupuesto por cada año

# Mostrar los datos del problema en una tabla con un cuadro
st.subheader("Datos del problema")
st.markdown("""
<div style="background-color: #333333; padding: 15px; border-radius: 10px; border: 2px solid #4682b4; color: #FFFFFF;">
    <h4 style="color: #4682b4;">Detalles de los Proyectos y Costos por Año</h4>
</div>
""", unsafe_allow_html=True)
data = {
    "Proyecto": [f"P{i+1}" for i in range(6)],
    "NPV": npv,
    "Año 1": [costs[0][i] for i in range(6)],
    "Año 2": [costs[1][i] for i in range(6)],
    "Año 3": [costs[2][i] for i in range(6)],
    "Año 4": [costs[3][i] for i in range(6)],
    "Año 5": [costs[4][i] for i in range(6)]
}
df = pd.DataFrame(data)
st.write(df)

# Crear el problema de maximización
model = LpProblem("Maximizar_NPV", LpMaximize)

# Definir variables binarias de decisión para cada proyecto
x = [LpVariable(f"x{i+1}", cat="Binary") for i in range(6)]

# Función objetivo: maximizar el NPV total
model += lpSum(npv[i] * x[i] for i in range(6)), "NPV_Total"

# Restricciones de presupuesto para cada año
for year in range(5):
    model += lpSum(costs[year][i] * x[i] for i in range(6)) <= budgets[year], f"Presupuesto_Año_{year+1}"

# Resolver el modelo
model.solve()

# Mostrar los resultados en un cuadro destacado
st.subheader("Resultados")
estado = "Óptimo" if model.status == 1 else "No Óptimo"
st.markdown(f"""
<div style="background-color: #444444; padding: 15px; border-radius: 10px; border: 2px solid #32CD32; color: #FFFFFF;">
    <p><strong>Estado del problema:</strong> {estado}</p>
    <p><strong>Valor óptimo de NPV:</strong> {value(model.objective)}</p>
</div>
""", unsafe_allow_html=True)

# Mostrar qué proyectos fueron seleccionados y cuáles no
seleccionados = []
no_seleccionados = []
for i in range(6):
    if x[i].value() == 1:
        seleccionados.append(f"Proyecto {i+1}")
    else:
        no_seleccionados.append(f"Proyecto {i+1}")

# Cuadro de proyectos seleccionados
st.markdown("""
<div style="background-color: #333333; padding: 15px; border-radius: 10px; border: 2px solid #FFA500; color: #FFFFFF;">
    <h4 style="color: #FFA500;">Proyectos Seleccionados</h4>
</div>
""", unsafe_allow_html=True)
for proyecto in seleccionados:
    st.markdown(f"<p style='color: #FFA500;'><strong>{proyecto}</strong></p>", unsafe_allow_html=True)

# Cuadro de proyectos no seleccionados
st.markdown("""
<div style="background-color: #333333; padding: 15px; border-radius: 10px; border: 2px solid #FF4500; color: #FFFFFF;">
    <h4 style="color: #FF4500;">Proyectos No Seleccionados</h4>
</div>
""", unsafe_allow_html=True)
for proyecto in no_seleccionados:
    st.markdown(f"<p style='color: #FF4500;'><strong>{proyecto}</strong></p>", unsafe_allow_html=True)
