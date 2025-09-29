lista_pessoas = [
    ["Lorenzo", "19999999999", "92900000", "lorenzo@email.com"],
]

while True:

    continuar = input("Deseja adicionar pessoas? (sim/nao): ")

    if continuar == "nao":
        break
    elif continuar == "sim":
        print("")
    else:
        print("Opção invalida")
        continue

    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    edv = input("Digite o edv: ")
    email = input("Digite o email: ")

    lista_pessoas.append([nome, telefone, edv, email])




while True:
    opcao = input("Escolha a opção: " \
    "\n1- Vizualizar todas as pessoas" \
    "\n2- Vizualizar pessoa especifica" \
    "\n3- Deletar uma pessoa especifica" \
    "\n4- Sair"
    "\nOpção: ")
    
    if opcao == "1":
        print(lista_pessoas)
    elif opcao == "2":
        indice = int(input("Digite o indice da pessoa: "))
        print(lista_pessoas[indice])

    elif opcao == "3":
        indice = int(input("Digite o indice da pessoa que será deletada: "))
        lista_pessoas.pop(indice)
    
    elif opcao == "4":
        break
    
    else:
        print("Opção invalida")
        continue
    
    input()