import random

random.seed() # inicializar com o OS


max=int(input('Insira um número máximo maior que 0 \n'))
if max < 0:
    print('erro')
    exit()
n1=random.randint(0,max)
count=0 #contar o numero de tentativas que o utilizador demora ate acertar
while True:
    palpite=int(input('Insira o seu palpite \n')) #palpite do utilizador
    count+=1 #incremento do contador
    if palpite ==n1:
        print('Acertou em ', count, ' vezes ') #vai dizer que acertou em que o utilizador acertou
        print('O número é', n1)
        exit()
    elif palpite <n1:
        print('O palpite é muito pequeno...')
    else:
        print('O palpite é muito grande')