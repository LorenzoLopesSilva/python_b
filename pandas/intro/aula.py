import datetime
import pandas as pd
import smtplib
import pywhatkit

def menu():
    try:
        print("Bem-vindo ao programa! \nQual opção você deseja?")
        print("1-HTML\n2-Excel\n4-Zap\n5-Sair")

        op = int(input("Digite a opção: "))

        if op == 1:
            pass
        elif op == 2:
            criar_excel()
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            print("Saiu")
    except ValueError:
        print("Opção inválida!")
        menu()

def ler_dados():
    dados = pd.read_csv('teste.csv')
    return dados

def criar_excel():
    dados_excel = ler_dados()

    caminho = "relatorio.xlsx"

    dados_excel.to_excel(caminho, index=False)

def enviar_email():
    email = "lorenzo.lopes0808@gmail.com"
    destinatario = input("Digite o email do destinatario")
    assunto = "Atualizações de estoque"

    dados = ler_dados()

    mensagem = "Segue o estoque atualizado: " + dados

    text = f"Subject: {assunto}\n\n{mensagem}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, ) #colocar seu email e a senha gerada no goolge account

# def zap():
#     try:
#         horas_atuais = datetime.datetime.now().hour
#         minutos_atuais = datetime.datetime.now().minute

#         dados = ler_dados()

#         pywhatkit.sendwhatmsg("+551979797979", dados, horas_atuais, minutos_atuais)


ler_dados()
criar_excel()
