import streamlit as st
import pulp
import time

st.title("Ejercicio 8.2: Tiempo de Cálculo para Problema LP")

st.write("""
Comparación del tiempo de cálculo entre el problema LP continuo y el problema LP con restricciones enteras.
""")

# Problema LP Continuo
prob_lp = pulp.LpProblem("Maximizar_P_LP", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)

prob_lp += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob_lp += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob_lp += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob_lp += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

start_time = time.time()
prob_lp.solve()
end_time = time.time()
tiempo_calculo_lp = end_time - start_time

estado_lp = pulp.LpStatus[prob_lp.status]
valor_objetivo_lp = pulp.value(prob_lp.objective)

st.subheader("Resultados para el problema LP continuo:")
st.markdown(f"""
<div style="background-color: #d1e7dd; padding: 15px; border-radius: 10px; border: 2px solid #0f5132; color: #0f5132;">
    <p><strong>Tiempo de cálculo:</strong> {tiempo_calculo_lp:.4f} segundos</p>
    <p><strong>Estado del problema LP:</strong> {estado_lp}</p>
    <p><strong>Valor óptimo de la función objetivo LP:</strong> {valor_objetivo_lp}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #cfe2ff; padding: 10px; border-radius: 10px; border: 2px solid #084298; color: #084298;">
    <p><strong>Valores óptimos de las variables de decisión (LP continuo):</strong></p>
</div>
""", unsafe_allow_html=True)

for variable in prob_lp.variables():
    st.markdown(f"<p style='color: #084298;'><strong>{variable.name} = {variable.varValue}</strong></p>", unsafe_allow_html=True)

# Problema LP con Enteros
prob_entero = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

prob_entero += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob_entero += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob_entero += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob_entero += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

start_time = time.time()
prob_entero.solve()
end_time = time.time()
tiempo_calculo_entero = end_time - start_time

estado_entero = pulp.LpStatus[prob_entero.status]
valor_objetivo_entero = pulp.value(prob_entero.objective)

st.subheader("Resultados para el problema LP con restricciones enteras:")
st.markdown(f"""
<div style="background-color: #fff3cd; padding: 15px; border-radius: 10px; border: 2px solid #664d03; color: #664d03;">
    <p><strong>Tiempo de cálculo:</strong> {tiempo_calculo_entero:.4f} segundos</p>
    <p><strong>Estado del problema LP con enteros:</strong> {estado_entero}</p>
    <p><strong>Valor óptimo de la función objetivo (Entero):</strong> {valor_objetivo_entero}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #e2e3e5; padding: 10px; border-radius: 10px; border: 2px solid #6c757d; color: #6c757d;">
    <p><strong>Valores óptimos de las variables de decisión (LP con enteros):</strong></p>
</div>
""", unsafe_allow_html=True)

for variable in prob_entero.variables():
    st.markdown(f"<p style='color: #6c757d;'><strong>{variable.name} = {variable.varValue}</strong></p>", unsafe_allow_html=True)
