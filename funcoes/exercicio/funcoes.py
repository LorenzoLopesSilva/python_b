import random

cartas = [
    ("2 de Copas", 2),
    ("2 de Ouros", 2),
    ("2 de Espadas", 2),
    ("2 de Paus", 2),
    
    ("3 de Copas", 3),
    ("3 de Ouros", 3),
    ("3 de Espadas", 3),
    ("3 de Paus", 3),

    ("4 de Copas", 4),
    ("4 de Ouros", 4),
    ("4 de Espadas", 4),
    ("4 de Paus", 4),

    ("5 de Copas", 5),
    ("5 de Ouros", 5),
    ("5 de Espadas", 5),
    ("5 de Paus", 5),

    ("6 de Copas", 6),
    ("6 de Ouros", 6),
    ("6 de Espadas", 6),
    ("6 de Paus", 6),

    ("7 de Copas", 7),
    ("7 de Ouros", 7),
    ("7 de Espadas", 7),
    ("7 de Paus", 7),

    ("8 de Copas", 8),
    ("8 de Ouros", 8),
    ("8 de Espadas", 8),
    ("8 de Paus", 8),

    ("9 de Copas", 9),
    ("9 de Ouros", 9),
    ("9 de Espadas", 9),
    ("9 de Paus", 9),

    ("A de Copas", 10),
    ("A de Ouros", 10),
    ("A de Espadas", 10),
    ("A de Paus", 10),

    ("K de Copas", 10),
    ("K de Ouros", 10),
    ("K de Espadas", 10),
    ("K de Paus", 10),

    ("Q de Copas", 10),
    ("Q de Ouros", 10),
    ("Q de Espadas", 10),
    ("Q de Paus", 10),

    ("J de Copas", 10),
    ("J de Ouros", 10),
    ("J de Espadas", 10),
    ("J de Paus", 10),
 
]

def iniciar_menu():
    escolha = int(input("Escolha uma opção: " \
    "\n1- Iniciar Jogo" \
    "\n2- Sair"))

    if escolha == 1:
        pass
    elif escolha == 2:
        pass
    else:
        print("Escolha invalida")
        iniciar_menu()


def escolher_carta(cartas):
    return random.choice(cartas)


    