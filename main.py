nome = input("Olá! Digite seu nome: ")
print(f"Olá {nome}! Tudo bem? Essa é uma calculadora que estou desenvolvendo!")
print("A calculadora pode estar bem básica por agora, mas futuramente ela será capaz de resolver grandes operações!")
print(f"Ok {nome}, qual operação você quer fazer?")
conta = input("Digite 1 para adição \nDigite 2 para subtração \nDigite 3 para multiplicação \nDigite 4 para divisão \nDigite aqui: ")

if conta == 1:
    num1 = Int(input("Digite seu número aqui: "))
    num2 = Int(input("Digite seu número aqui: "))
    print(num1 + num2)