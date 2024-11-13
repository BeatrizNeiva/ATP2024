# criar lista com números do usuário
def criar_lista_usuario():
    lista = []
    n = int(input("Quantos números deseja adicionar à lista? "))
    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista.append(numero)
    return lista

# exibir o menu e as opções
def menu():
    lista = []
    continuar = True
    while continuar:
        print("\nMenu:")
        print("(1) Criar Lista")
        print("(2) Ler Lista")
        print("(3) Soma")
        print("(4) Média")
        print("(5) Maior")
        print("(6) Menor")
        print("(7) Está Ordenada Crescente")
        print("(8) Está Ordenada Decrescente")
        print("(9) Procurar Elemento")
        print("(0) Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            lista = criar_lista_usuario()
            print("Lista criada:", lista)
        
        elif escolha == 2:
            print("Lista atual:", lista)
        
        elif escolha == 3:
            print("Soma:", sum(lista))
        
        elif escolha == 4:
            print("Média:", sum(lista) / len(lista) if lista else 0)
        
        elif escolha == 5:
            print("Maior:", max(lista) if lista else "Lista vazia")
        
        elif escolha == 6:
            print("Menor:", min(lista) if lista else "Lista vazia")
        
        elif escolha == 7:
            print("Está ordenada de forma crescente?", "Sim" if lista == sorted(lista) else "Não")
        
        elif escolha == 8:
            print("Está ordenada de forma decrescente?", "Sim" if lista == sorted(lista, reverse=True) else "Não")
        
        elif escolha == 9:
            elemento = int(input("Digite o número a procurar: "))
            print("Elemento encontrado na posição:", lista.index(elemento) if elemento in lista else "Elemento não encontrado")
        
        elif escolha == 0:
            print("Saindo. Lista final:", lista)
            continuar = False  # sair do loop

        else:
            print("Opção inválida!")


menu()
