# Função auxiliar para validar entradas numéricas
def coletar_numero(mensagem, tipo):
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print(f"Por favor, insira um número válido para {tipo.__name__}.")

# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ")

    # Coleta da idade e peso do pet utilizando a função auxiliar
    idade = coletar_numero("Idade do pet (em anos): ", int)
    peso = coletar_numero("Peso do pet (em kg): ", float)

    # Exibindo as informações coletadas
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

# Chama a função para coletar e exibir as informações do pet
coletar_informacoes_pet()
