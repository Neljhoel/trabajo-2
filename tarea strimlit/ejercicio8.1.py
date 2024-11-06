import streamlit as st
import pulp

# Título de la aplicación
st.title("Ejercicio 8.1: Método Branch and Bound")

# Descripción del problema con un cuadro de información
st.markdown("""
<div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 2px solid #4CAF50; color: #FFFFFF;">
    <h4 style="color: #4CAF50;">Descripción del Problema</h4>
    <p><strong>Resolver el problema de maximización usando el Método Branch and Bound:</strong></p>
    <p><strong>Maximizar:</strong> <br> <code>P(x1, x2, x3) = 4x1 + 3x2 + 3x3</code></p>
    <p><strong>Sujeto a:</strong></p>
    <ul>
        <li><code>4x1 + 2x2 + x3 <= 10</code></li>
        <li><code>3x1 + 4x2 + 2x3 <= 14</code></li>
        <li><code>2x1 + x2 + 3x3 <= 7</code></li>
        <li><code>x1, x2, x3</code> son enteros no negativos</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Definir el problema de optimización
prob = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

# Definir variables de decisión
x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

# Definir la función objetivo y restricciones
prob += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

# Resolver el problema
prob.solve()

# Resultados
estado = pulp.LpStatus[prob.status]
valor_objetivo = pulp.value(prob.objective)

# Mostrar resultados en un cuadro destacado
st.subheader("Resultados:")
st.markdown(f"""
<div style="background-color: #333333; padding: 20px; border-radius: 10px; border: 2px solid #FF8C00; color: #FFFFFF;">
    <h4 style="color: #FF8C00;">Estado del Problema</h4>
    <p><strong>Estado:</strong> {estado}</p>
    <p><strong>Valor óptimo de la función objetivo:</strong> {valor_objetivo}</p>
</div>
""", unsafe_allow_html=True)

# Mostrar valores de las variables en un contenedor con estilo
st.subheader("Valores Óptimos de las Variables de Decisión")
st.markdown("""
<div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; border: 2px solid #87CEEB; color: #FFFFFF;">
""", unsafe_allow_html=True)
for variable in prob.variables():
    st.markdown(f"<p style='color: #87CEEB;'><strong>{variable.name} = {variable.varValue}</strong></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
