def calcula_digitos(num):
    digitos = 0
    if num < 0:
        num = num * -1
    while num != 0:
        digitos +=1
        num= num //10

    # quando chegamos aqui digitios possui o numero de digitos
    return digitos

while True:
    valor=int(input('Insira um número (0 para sair):'))
    if valor == 0:
        break
    print(f'o número {valor} possui {calcula_digitos(valor)} digitos')

print('Adeus!')