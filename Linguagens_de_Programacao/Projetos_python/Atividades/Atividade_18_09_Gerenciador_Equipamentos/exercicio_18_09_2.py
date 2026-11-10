equipamentos = []

while True:
    print("GERENCIADOR DE EQUIPAMENTOS")
    print("1 - Cadastrar equipamentos")
    print("2 - Mostrar Equipamentos")
    print("3 - Mostrar quantidade de equipamentos")
    print("4 - Consultar equipamento")
    print("5 - Remover equipamento")
    print("6 - Sair")

    opcao=input("digite o numero desejado: ")
    print("-" *40)

    if opcao=='1':
        contador = 0
        meta = 5
        for i in range(5):
            contador += 1
            print("TELA DE CADASTRO")
            # Cria Equipamento
            equip= input("Digite o nome do {contador} equipamento, (Ex: Notebook): ")
            equipamentos.append(equip)
            # Verificação se bateu a meta
            if contador >= meta:
                break

    elif opcao=='2':
            if len(equipamentos) == 0:
                print("Não tem nenhum equipamento cadastrado")
            else:
                print(equipamentos)
    
    elif opcao=='3':
            if len(equipamentos) == 0:
                print("Não tem nenhum equipamento cadastrado")
            else:
                print(len(equipamentos))

    elif opcao=='4':
            

            
            # Remover Equipamento (1 por vez)
            remover=input(f"Digite qual equipamento quer remover da seguinte lista: {equipamentos}")
            equipamentos.remove(remover)
            # print(equipamentos) - tirei
    
    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Digite um número de 1 a 4.")
        input("Aperte ENTER para tentar de novo...")