num=int(input('Insira um numero inteiro: '))
numero_original = num
contador = 0

if num < 0:
    print('Erro, a sair do programa...')
    exit()

while num!= 0:
    num = num // 10
    contador += 1
print(' O numero', numero_original, 'possui', contador, 'digitos!')