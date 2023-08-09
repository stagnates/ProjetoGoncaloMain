# Função para mostrar a ementa atual
def mostrar_ementa(ementa):
    print("Ementa do dia: \n")
    for prato in ementa:
        print(f"{prato}")
    print()

# Função para adicionar um prato à ementa
def adicionar_prato(ementa, novo_prato):
    ementa.append(novo_prato)
    print(f"{novo_prato} foi adicionado à ementa.\n")

# Função para retirar um prato da ementa
def retirar_prato(ementa, prato_retirar):
    if prato_retirar in ementa:
        ementa.remove(prato_retirar)
        print(f"{prato_retirar} foi retirado da ementa.\n")

# Ementa inicial
ementa_do_dia = ["Arroz com ovo", "Arroz com atum", "Esparguete à bolonhesa", "Lulas recheadas"]

# Mostrar a ementa atual
mostrar_ementa(ementa_do_dia)

# Adicionar um prato à ementa
novo_prato = "Frango de Caril"
adicionar_prato(ementa_do_dia, novo_prato)
mostrar_ementa(ementa_do_dia)

# Retirar um prato da ementa
prato_retirar = "Arroz com atum"
retirar_prato(ementa_do_dia, prato_retirar)
mostrar_ementa(ementa_do_dia)
