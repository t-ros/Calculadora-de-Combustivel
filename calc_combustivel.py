#  Um simples script para ajudar a saber
#  @ 2025 by Diogo "Teros" Monteiro 

def main():
    
    print("Estimativa de Combustivel Consumido")
    
    distancia = float(input("Digite a distância da viagem (km): "))
    consumo_medio = float(input("Digite o consumo médio do carro (litros/100km): "))
    preco = float(input("Digite o preço do combustivel (€/litro): "))
    
    litros = (distancia * consumo_medio) / 100
    custo = litros * preco
    
    print(f"Custo da Viagem: {custo:.2f}€")
    return 0


if __name__ == '__main__':
    main()
