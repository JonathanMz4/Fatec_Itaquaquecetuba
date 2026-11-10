equipamentos = []
contador = 0
meta = 5

for i in range(5):
    contador += 1
    equip=input(f"Digite o nome do {contador} equipamento:")
    equipamentos.append(equip)
    if contador >= meta:
        print(equipamentos)
        print(len(equipamentos))
        if "Servidor" in equipamentos:
            print("Servidor está dentro de equipamentos")
        else:
            print("Servidor não está dentro de equipamentos")
        remover=input(f"Digite qual equipamento quer remover da seguinte lista: {equipamentos}")
        equipamentos.remove(remover)
        print(equipamentos)
        break
