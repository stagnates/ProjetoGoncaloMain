def calcular_media_ponderada():
    nota1= 12
    nota2= 14
    peso1= 100
    media_ponderada = (nota1 * peso1 + nota2 * (100 - peso1)) / 100
    return media_ponderada
    print(f'a média é {media_ponderada}')
  