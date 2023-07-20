#https://wiki.python.org.br/EstruturaSequencial

"""
#Ex.1
print("Alo Mundo")

print("--"*10)
"""

""""#Ex.2
numero1 = int (input("Digite um número: "))
print (f'O número informado foi {numero}')

print("--"*10)
"""

"""
#Ex.3
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
resultado = num1 + num2
print(f'A soma de {num1} com {num2} é igual a {resultado}')

print("--"*10)
"""

"""
#Ex.4

nota1=float(input('Insira a primeira nota: '))
nota2=float(input('Insira a segunda nota: '))
nota3=float(input('Insira a terceira nota: '))
nota4=float(input('Insira a quarta nota: '))

def calcular_media(nota1, nota2, nota3, nota4):
    print('Notas: ', nota1, nota2, nota3, nota4)
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

media = calcular_media(nota1, nota2, nota3, nota4)
print(f'A média das notas é {media}')
"""

"""
#Ex.5
num = float(input('Insira um valor em metros: '))
centimetros = num * 100;

print(f'O valor que inseriu corresponde a {centimetros} centimetros')
"""

"""
#Ex.6
raio = float(input('Insira o raio de um circulo: '))

area = 3.141592653589793 * raio ** 2
print(f'A area é de {area:4.4f}')
"""

"""
#Ex.7
lado = float(input('Insira a altura do quadrado:\n'))

area_quadrado = lado**2
dobro_area = 2 * area_quadrado

print(f'O dobro da área do quadrado é de {dobro_area} ')
"""

"""
#Ex.8

valor_hora = int(input('Insira o valor recebido por hora:\n'))
horas_trabalhadas = int(input('Insira as horas trabalhadas:\n'))

def total_salario_mes():

     salario_mensal = (valor_hora * horas_trabalhadas)
     return salario_mensal

salario_mensal = total_salario_mes()
print(f'Total do salário no mês: {salario_mensal}')
"""

"""
#Ex9
graus_celsius = float(input('Insira a temperatura em Fahrenheit: \n '))

celcius = 5*((graus_celsius-32)/9)
print(f'A temperatura em graus Celsius é {celcius}')
"""

"""
#Ex.10
graus_farenheit = float(input('Insira a temperatura em Celsius: \n '))

farenheit =(graus_farenheit * 9/5) + 32
            
print(f'A temperatura em graus farenheit é {farenheit}')
"""

"""
#Ex.11
num1 = int(input('Insira o primeiro número inteiro: '))
num2 = int(input('Insira o segundo número inteiro: '))
num3 = float(input('Insira um número real: '))

a = (num1*2)*(num2/2)
b = (num1*3)+(num3)
c = (num3**3)

print(f'O produto do dobro do primeiro com metado do segundo é {a}')
print(f'A soma do triplo do primeiro com o terceiro é {b}')
print(f'O terceiro elevado ao cubo é {c}')
"""

"""
#Ex.12
altura  = float(input('Insira a sua altura: '))

peso_ideal = (72.7*altura) - 58

print(f'O seu peso ideal é {peso_ideal}')
"""

"""
#Ex.13
altura  = float(input('Insira a sua altura: '))

peso_ideal_homem = (72.7*altura) - 58
peso_ideal_mulher = (62.1*altura) - 44.7

print(f'O seu peso ideal para homem é {peso_ideal_homem}')
print(f'O seu peso ideal para mulher é {peso_ideal_mulher}')
"""

""""
#Ex.14
peso_peixe = float(input("Insira o peso do peixe em quilos: "))

limite_peso = 50
valor_multa = 4.00

if peso_peixe > limite_peso:
    excesso = peso_peixe - limite_peso
    multa = excesso * valor_multa
else:
    excesso = 0
    multa = 0
print(f'O peso do peixe corresponde a {peso_peixe} quilos')
print(f'O exceso de peso corresponde a {excesso} quilos')
print(f'Valor da multa a ser pago: R$ {multa}')
"""

"""
#Ex.15

ganho_hora = float(input('Ganho por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))

salario_bruto = ganho_hora * horas_trabalhadas
Imposto_Renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - Imposto_Renda - inss - sindicato

print(f'O seu salário bruto corresponde a {salario_bruto} R$')
print(f'O Imposto de Renda (11%) corresponde a {Imposto_Renda} R$')
print(f'O seu salário INSS (8%) corresponde a {inss}')
print(f'O imposto do sindicato (5%) corresponde a {sindicato} R$')
print(f'O seu salário líquido corresponde a {salario_liquido} R$')
"""

#Ex.16
import math
metros_quadrados_area = float(input('Insira um valor para os metros quadrados da área a ser pintada: '))

litros_tinta = metros_quadrados_area / 3

quantidade_latas_tinta = int(litros_tinta / 18)
if litros_tinta % 18 !=0:
    quantidade_latas_tinta += 1

preco_total = quantidade_latas_tinta * 80.00

print(f'A quantidade de latas de tinta que precisa de comprar são {quantidade_latas_tinta}')
print(f'O preço total a pagar são {preco_total} R$')