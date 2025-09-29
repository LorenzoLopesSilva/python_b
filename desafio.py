import reportlab.lib.pagesizes as pagesizes

from reportlab.pdfgen import canvas

contatos = [
    {
        "nome": "Lorenzo",
        "telefone": "19983659999",
        "edv": "1234",
        "email": "lorenzo@teste"
    },
    {
        "nome": "Wilson",
        "telefone": "1998070707",
        "edv": "9999",
        "email": "wilson@email"
    }
]

senha_admin = "admin"
senha_user = "1234"

while True:
    senha = input("Digite a senha (Enter para encerrar): ")

    if senha == senha_admin:
        admin = True
    elif senha == senha_user:
        admin = False
    elif senha == "":
        break
    else:
        print("Senha incorreta!")
        continue



    if(admin):

        while True:
            continuar = input("Deseja adicionar uma pessoa? (s/n): ")

            if continuar == "s":
                print("")
            elif continuar == "n":
                break
            else:
                print("Opção invalida")
                continue

            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            edv = input("Digite o edv: ")
            email = input("Digite o email: ")

            contatos.append({"nome": nome, "telefone": telefone, "edv": edv, "email": email})

        while True:
            opcao = input("Escolha a opção: " \
            "\n1- Vizualizar todas as pessoas" \
            "\n2- Vizualizar pessoa especifica" \
            "\n3- Deletar uma pessoa especifica" \
            "\n5- Sair"
            "\nOpção: ")

            #define os edvs
            edvs = []
            for i in contatos:
                edvs.append(i["edv"])

            
            if opcao == "1":
                print(contatos)

            elif opcao == "2":
                edv = input("Digite o edv da pessoa: ")
                indice = edvs.index(edv)
                print(contatos[indice])

            elif opcao == "3":
                edv = input("Digite o edv da pessoa: ")
                indice = edvs.index(edv)
                contatos.pop(indice)
                print("Contato deletado!")
            
            elif opcao == "4":
                page_size = pagesizes.letter

                canvas = canvas.Canvas('example.pdf')

                canvas.setPageSize(page_size)

                text = str(contatos)

                canvas.drawString(100, 750, text)

                canvas.showPage()
                canvas.save()
            
            elif opcao == "5":
                break
                
            else:
                print("Opção invalida")
                continue
            
            input()
        
    else:
        while True:
            edv = input("Digite o edv para consulta (Enter para sair): ")
            edvs = []
            for i in contatos:
                edvs.append(i["edv"])

            if edv in edvs:
                indice = edvs.index(edv)
                print(contatos[indice])
                input()
                continue
            elif edv == "":
                break
            else:
                print("Usuario não encontrado")
                continue
        
