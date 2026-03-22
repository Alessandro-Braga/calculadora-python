nome = input("Olá! Digite seu nome: ")
print(f"Olá {nome}! Tudo bem? Essa é uma calculadora que estou desenvolvendo!")
print("A calculadora pode estar bem básica por agora, mas futuramente ela será capaz de resolver grandes operações!")
print(f"Ok {nome}, qual operação você quer fazer?")
conta = int(input("Digite 1 para adição \nDigite 2 para subtração \nDigite 3 para multiplicação \nDigite 4 para divisão \nDigite aqui: "))
print("Ok, agora, me diga os números")
num1 = int(input("Digite seu número aqui: "))
num2 = int(input("Digite seu número aqui: "))

if conta == 1:
    print(f"Seu resultado: {num1 + num2}")

elif conta == 2:
    print(f"Seu resultado: {num1 - num2}")

elif conta == 3:
    print(f"Seu resultado: {num1 * num2}")

else:
    print("Você quer fazer uma divisão exata (sem casas decimais) ou uma divisão não exata (com casas decimais)?")
    div = int(input("Digite 1 para divisão exata \nDigite 2 para divisão não exata"))
    if div == 1:
        print(f"Seu resultado: {num1 // num2}")
    else:
        print(f"Seu resultado: {num1 / num2}")