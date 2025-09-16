import streamlit as st

st.title("Calculadora de Combustível")

distancia = st.number_input("Distância da viagem (km)", min_value=0.0)
consumo_medio = st.number_input("Consumo médio do carro (L/100km)", min_value=0.0)
preco_combustivel = st.number_input("Preço do combustível (€/L)", min_value=0.0)

if st.button("Calcular"):
    litros_necessarios = (distancia * consumo_medio) / 100
    custo_total = litros_necessarios * preco_combustivel
    st.write(f"➡ Combustível necessário: {litros_necessarios:.2f} litros")
    st.write(f"➡ Custo total da viagem: {custo_total:.2f} €")
