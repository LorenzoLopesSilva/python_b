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
    escolha_iniciar = int(input("Digite sua escolha: " \
    "\n 1- Iniciar" \
    "\n 2- Sair" \
    "\n"))

    if escolha_iniciar == 1:
        iniciar_jogo()
    elif escolha_iniciar == 2:
        pass
    else:
        print("Escolha invalida")
        iniciar_menu()
    
def escolher_carta(cartas):
    carta = random.choice(cartas)
    carta_nome = carta[0]
    valor_carta = carta[1]
    print(carta_nome)
    return valor_carta

def iniciar_jogo(cartas):
    print("Cartas do Usuario: ")
    carta_1 = escolher_carta(cartas)
    carta_2 = escolher_carta(cartas)
    cartas_usuario = carta_1 + carta_2
    print(f"Total: {cartas_usuario}")

    print("\nCartas do Dealer: ")
    carta_dealer_1 = escolher_carta(cartas)
    carta_dealer_2 = escolher_carta(cartas)
    cartas_dealer = carta_dealer_1 + carta_dealer_2
    print(f"Total: {cartas_dealer}")



    escolha_menu()
    print("teste jogo")

def escolha_menu():
    print("teste escolha")


iniciar_jogo(cartas)
