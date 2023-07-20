
def calcular_factorial(n):
    total = 1 # nao pode ser 0!!!
    for i in range(n, 0, -1):
        total *= i

    return total


while True:
    menu = int(input('Selecione um opção:\n1-fatorial\n0-Sair\n: '))
    match menu: #ele nao suporta mas é assim que funciona na maior versao
        case 1:
            valor = int(input('Insira um valor: '))
            print(f'Resultado: {calcular_factorial(valor)}')
        case 0:
            exit()
        case _:
            print('Erro! Repita!')