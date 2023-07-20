def adicionar():
    num1 = int(input("Escreva o primeiro número: "))
    num2 = int(input("Escreva o segundo número: "))
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é igual a {resultado}")

def multiplicar():
    num1 = int(input("Escreva o primeiro número: "))
    num2 = int(input("Escreva o segundo número: "))
    resultado = num1 * num2
    print(f"O produto de {num1} e {num2} é igual a {resultado}")

def calcular_fatorial():
    num = int(input("Escreva um número inteiro: "))
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é igual a {fatorial}")

def calcular_soma():
    num = int(input("Escreva um número inteiro: "))
    soma = sum(range(num + 1))
    print(f"A soma de todos os números inteiros entre 0 e {num} é igual a {soma}")

while True:
    print("Escolha uma opção:")
    print("1 - Adicionar dois numeros inteiros")
    print("2 - Multiplicar dois numeros inteiros")
    print("3 - Calcular o fatorial de um número inteiro")
    print("4 - Calcular a soma de todos os números inteiros entre 0 e n")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        adicionar()
    elif opcao == 2:
        multiplicar()
    elif opcao == 3:
        calcular_fatorial()
    elif opcao == 4:
        calcular_soma()
    elif opcao == 0:
        print("bye bye")
        break
    else:
        print("Escolha inválida!")
