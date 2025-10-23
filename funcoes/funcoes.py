def soma_dois_numeros():
    n1 = 10
    n2 = 45

    s = n1 + n2

    return s

def mostrar_menu():
    print("1- Iniciar")
    print("2- Sair")
    print("3- Credito")

    escolha = int(input(" "))

    if escolha == 1:
        iniciar()
    elif escolha == 2:
        sair()
    else:
        creditos()

def iniciar():
    print("Programa iniciado")


def sair():
    print("Programa fechado")


def creditos():
    print("Lorenzo")
