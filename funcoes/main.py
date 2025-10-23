# import funcoes2
from funcoes import mostrar_menu
# from funcoes2 import soma_dois_numeros
from funcoes import soma_dois_numeros as funcao_importada
# def soma_dois_numeros():
#     n1 = 10
#     n2 = 45

#     s = n1 + n2

#     print(f"A soma é igual a {s}")

# if __name__ == "__main__":
#     soma_dois_numeros()

#-------------------------------------------------------------------------------------

# def soma_dois_numeros_com_parametros(n1: int, n2: int):
#     s = n1 + n2
#     print(f"Soma: {s}")

# numero_1 = int(input("Digite um numero: "))
# numero_2 = int(input("Digite um numero: "))

# soma_dois_numeros_com_parametros(n1=numero_1, n2=numero_2)

#--------------------------------------------------------------------------------------

# def soma_dois_numeros_parametros_opcionais(n1: int = 36, n2: int = 12):
#     s = n1 + n2
#     return s, n1, n2

# soma, num1, num2 = soma_dois_numeros_parametros_opcionais()

# print(soma)

# print(funcao_importada())

if __name__ == "__main__":
    mostrar_menu()