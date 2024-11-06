import streamlit as st
import pulp

st.title("Ejercicio 8.3: Minimización usando Cortes de Gomory")

# Descripción del problema en un cuadro de información
st.markdown("""
<div style="background-color: #333333; padding: 20px; border-radius: 10px; border: 2px solid #4CAF50; color: #FFFFFF;">
    <h4 style="color: #4CAF50;">Descripción del Problema</h4>
    <p><strong>Resolver el siguiente problema de minimización usando cortes de Gomory de manera iterativa:</strong></p>
    <p><strong>Minimizar:</strong> <br> <code>C(x, y) = x - y</code></p>
    <p><strong>Sujeto a:</strong></p>
    <ul>
        <li><code>3x + 4y <= 6</code></li>
        <li><code>x - y <= 1</code></li>
        <li><code>x, y</code> son enteros no negativos</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Definición del problema de optimización
prob_gomory = pulp.LpProblem("Minimizar_C", pulp.LpMinimize)

x = pulp.LpVariable("x", lowBound=0, cat="Integer")
y = pulp.LpVariable("y", lowBound=0, cat="Integer")

prob_gomory += x - y, "Función Objetivo"
prob_gomory += 3 * x + 4 * y <= 6, "Restricción 1"
prob_gomory += x - y <= 1, "Restricción 2"

# Resolución del problema
prob_gomory.solve()

estado = pulp.LpStatus[prob_gomory.status]
valor_objetivo = pulp.value(prob_gomory.objective)

# Mostrar los resultados iniciales en un cuadro destacado
st.subheader("Resultados iniciales:")
st.markdown(f"""
<div style="background-color: #444444; padding: 15px; border-radius: 10px; border: 2px solid #FF8C00; color: #FFFFFF;">
    <p><strong>Estado del problema:</strong> {estado}</p>
    <p><strong>Valor óptimo de la función objetivo:</strong> {valor_objetivo}</p>
</div>
""", unsafe_allow_html=True)

# Mostrar valores de las variables de decisión en un cuadro
st.markdown("""
<div style="background-color: #555555; padding: 10px; border-radius: 10px; border: 2px solid #87CEEB; color: #FFFFFF;">
    <p><strong>Valores óptimos de las variables de decisión:</strong></p>
</div>
""", unsafe_allow_html=True)

for variable in prob_gomory.variables():
    st.markdown(f"<p style='color: #87CEEB;'><strong>{variable.name} = {variable.varValue}</strong></p>", unsafe_allow_html=True)

# Proceso de cortes de Gomory en un cuadro informativo
st.subheader("Proceso de cortes de Gomory")
st.markdown("""
<div style="background-color: #333333; padding: 15px; border-radius: 10px; border: 2px solid #DAA520; color: #FFFFFF;">
    <p>Para aplicar los cortes de Gomory:</p>
    <ol>
        <li>Observa la solución inicial de valores no enteros en las variables de decisión.</li>
        <li>Introduce un nuevo corte que elimine esta solución fraccionaria.</li>
        <li>Repite el proceso hasta obtener una solución entera.</li>
    </ol>
    <p><strong>Nota:</strong> Los cortes de Gomory no se realizan automáticamente en esta implementación. Puedes aplicar los cortes manualmente utilizando herramientas avanzadas como Excel o MATLAB, o resolverlos en un software especializado en programación lineal entera.</p>
</div>
""", unsafe_allow_html=True)
