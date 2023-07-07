def tabela_servicos(): # função que chama na tela o catálogo de opções de servicos adicionais
    valores = [
        {'Número': '1', 'Serviço': 'Cortar Unhas', 'Valor': 10},
        {'Número': '2', 'Serviço': 'Escovar Dentes', 'Valor': 12},
        {'Número': '3', 'Serviço': 'Limpar Orelhas', 'Valor': 15},
        {'Número': '0', 'Serviço': 'Não querer mais nada', 'Valor': 0}
    ]

    print("Serviços Adicionais:")
    for servico in valores:
        print(f"{servico['Número']} - {servico['Serviço']:<20} R$ {servico['Valor']:2}")

def cachorro_peso(): # função que recebe o peso do cachorro e retorna o valor de acordo com as métricas pré estabelecidas
    while True:
        try:
            peso = float(input("Digite o peso do seu cachorro em kg: "))
            if peso < 3:
                return 40
            elif peso >= 3 and peso < 10:
                return 50
            elif peso >=10 and peso < 30:
                return 60
            elif peso >= 30 and peso < 50:
                return 70
            else:
                print("Peso inválido! Por favor digite um valor menor que 50.")
        except ValueError:
            print("Valor inválido! Por favor digite um valor numérico.")

def cachorro_pelo(): # função que recebe a informação de tamanho do pelo do cachorro e retorna o multiplicador
    while True:
        pelo = input("Digite o tipo de pelo do seu cachorro (c - curto, m - médio, l - longo): ")
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Tipo de pelo inválido! Por favor digite 'c', 'm' ou 'l'.")

def cachorro_extra(): # função que recebe a informação dos serviços adicionais disponibilizados através do catálogo
    servicos_extras = {'1': 10, '2': 12, '3': 15} 
    valor_extra = 0
    while True:
        servico_adicional = input("Digite o número do serviço adicional que precisa (1 - cortar unhas, 2 - escovar dentes, 3 - limpar orelhas) ou 0 para nenhuma opção: ")
        print("Serviços Adicionais:")
        if servico_adicional in servicos_extras:
            valor_extra += servicos_extras[servico_adicional]
        elif servico_adicional == '0':
            return valor_extra
        else:
            print("Opção inválida! Por favor digite um número válido ou 0.")

def main():
    print("Bem-vindo ao Petshop da Jhenifer Ferreira Vaz!")

    tabela_servicos() # exibe o catálogo logo acima, antes do restante do código 

    valor_base = cachorro_peso()
    print(f"Valor base: R${valor_base:.2f}")

    multiplicador = cachorro_pelo()
    print(f"Tamanho do pelo: {multiplicador}")

    valor_extra = cachorro_extra()
    print(f"Valor extra: R${valor_extra:.2f}")

    total_pagar = valor_base * multiplicador + valor_extra
    print(f"Total a pagar: R${total_pagar:.2f}")
    print("Agradecemos a preferência!")

if __name__ == '__main__': # informa o que deve ser executado primeiro 
    main()
