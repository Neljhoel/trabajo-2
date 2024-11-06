import streamlit as st
import pulp

st.title("Ejercicio 8.4: Maximización usando Cortes de Gomory")

# Descripción del problema en un cuadro de información
st.markdown("""
<div style="background-color: #2E2E2E; padding: 20px; border-radius: 10px; border: 2px solid #1E90FF; color: #FFFFFF;">
    <h4 style="color: #1E90FF;">Descripción del Problema</h4>
    <p><strong>Resolver el siguiente problema de maximización usando cortes de Gomory de manera iterativa:</strong></p>
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

# Definición del problema de optimización
prob_gomory = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

prob_gomory += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob_gomory += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob_gomory += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob_gomory += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

# Resolución del problema
prob_gomory.solve()

estado = pulp.LpStatus[prob_gomory.status]
valor_objetivo = pulp.value(prob_gomory.objective)

# Mostrar los resultados iniciales en un cuadro destacado
st.subheader("Resultados iniciales:")
st.markdown(f"""
<div style="background-color: #4B4B4B; padding: 15px; border-radius: 10px; border: 2px solid #FFA500; color: #FFFFFF;">
    <p><strong>Estado del problema:</strong> {estado}</p>
    <p><strong>Valor óptimo de la función objetivo:</strong> {valor_objetivo}</p>
</div>
""", unsafe_allow_html=True)

# Mostrar valores de las variables de decisión en un cuadro
st.markdown("""
<div style="background-color: #3E3E3E; padding: 10px; border-radius: 10px; border: 2px solid #87CEEB; color: #FFFFFF;">
    <p><strong>Valores óptimos de las variables de decisión:</strong></p>
</div>
""", unsafe_allow_html=True)

for variable in prob_gomory.variables():
    st.markdown(f"<p style='color: #87CEEB;'><strong>{variable.name} = {variable.varValue}</strong></p>", unsafe_allow_html=True)

# Proceso de cortes de Gomory en un cuadro informativo
st.subheader("Proceso de cortes de Gomory")
st.markdown("""
<div style="background-color: #2E2E2E; padding: 15px; border-radius: 10px; border: 2px solid #DAA520; color: #FFFFFF;">
    <p>Para aplicar los cortes de Gomory:</p>
    <ol>
        <li>Observa la solución inicial de valores no enteros en las variables de decisión.</li>
        <li>Introduce un nuevo corte que elimine esta solución fraccionaria.</li>
        <li>Repite el proceso hasta obtener una solución entera.</li>
    </ol>
    <p><strong>Nota:</strong> Los cortes de Gomory no se realizan automáticamente en esta implementación. Puedes aplicar los cortes manualmente utilizando herramientas avanzadas como Excel o MATLAB, o resolverlos en un software especializado en programación lineal entera.</p>
</div>
""", unsafe_allow_html=True)
