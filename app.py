import streamlit as st


st.title("Calculadora de Combustível")

# Inputs
consumo_medio = st.number_input("Consumo médio do carro (L/100km)", min_value=0.0, max_value=50.0)
preco_combustivel = st.number_input("Preço do combustível (€/L)", min_value=0.0, max_value=3.0)
distancia = st.slider("Distância da viagem (km)", 0, 1000, 100)

# Cálculo

litros_necessarios = (distancia * consumo_medio) / 100
custo_total = litros_necessarios * preco_combustivel

# Output
st.info(f"Combustível necessário: {litros_necessarios:.2f} L")
st.success(f"Custo total da viagem: {custo_total:.2f} €")
