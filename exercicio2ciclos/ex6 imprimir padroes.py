num= int(input('Insira um número inteiro maior que zero: '))

if num <= 0:
    print('Erro no número inserido')
    exit()

for i in range(1, num +1):
    num= 1
    while num <= i:
        print(f'{num:<3d}', end='')
        num +=1
    print()