#Bibliotecas para criação de PDF
import reportlab.lib.pagesizes as pagesizes
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

#Lista de contatos inicial
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

#Definição de senha de usuario e admin
senha_admin = "admin"
senha_user = "1234"

#A interface começa a rodar
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
            opcao = input("Escolha a opção: " \
            "\n1- Adicionar nova pessoa" \
            "\n2- Vizualizar todas as pessoas" \
            "\n3- Vizualizar pessoa especifica" \
            "\n4- Deletar uma pessoa especifica" \
            "\n5- Salvar lista em PDF" \
            "\n6- Sair"
            "\nOpção: ")

            #define os edvs
            edvs = []
            for i in contatos:
                edvs.append(i["edv"])

            #Adicionar uma pessoa
            if opcao == "1":
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


            #Mostrar toda a lista de contatos
            elif opcao == "2":
                print(contatos)

            #Mostrar um contato especifico
            elif opcao == "3":
                try:
                    edv = input("Digite o edv da pessoa: ")
                    indice = edvs.index(edv)
                    print(contatos[indice])
                except:
                    print("EDV não encontrado")
                    input()
                    continue

            #Deletar um contato especifico        
            elif opcao == "4":
                try:
                    edv = input("Digite o edv da pessoa: ")
                    indice = edvs.index(edv)
                    contatos.pop(indice)
                    print("Contato deletado!")
                except ValueError:
                    print("EDV não encontrado")
                    input()
                    continue
            
            #Criar PDF
            elif opcao == "5":
                page_size = pagesizes.letter #define o tamanho da pagina
                canvas = canvas.Canvas('contatos.pdf') #Cria a tela
                canvas.setPageSize(page_size)
                textobject = canvas.beginText(inch, 10 * inch)

                #---Criação do conteudo da pagina
                textobject.textLine("Lista de contatos:")
                textobject.textLine("")
                textobject.textLine("")
                
                #Estrutura de cada contato
                for index_contato in contatos:
                    textobject.textLine("")
                    textobject.textLine(f"- Contato {contatos.index(index_contato) + 1}: ")
                    for a in index_contato:
                        textobject.textLine(
                            f"{a.capitalize()}: {index_contato[a]}"
                            )

                canvas.drawText(textobject)

                canvas.showPage() #finaliza a pagina atual
                canvas.save() #salva a pagina

                print("Lista salva com sucesso")
            
            #Sair
            elif opcao == "6":
                break

            #Em caso de opção invalida    
            else:
                print("Opção invalida")
                continue
            
            input()
    
    #Fim das opções de admin e opções de usuario    
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
        
