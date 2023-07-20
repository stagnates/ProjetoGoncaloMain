num=int(input('Insira um numero: '))
inv= 0
numero_original= num
while num>0:
    resto = num % 10
    inv = inv * 10 + resto
    num //= 10
print('Numero inserido: ', numero_original)
print('Numero inverso: ',inv)