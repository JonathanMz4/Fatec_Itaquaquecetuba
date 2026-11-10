Computador={"patrimonio": "Publico", "marca": "Lenovo", "modelo": "Thinkpad", "processador": "Intel", "memoria": "16gb", "armazenamento": "512gb", "sistema operacional": "Windows"}

print(Computador["modelo"])
print(Computador["memoria"])

novo = input("Altere a memoria para: ")
Computador["memoria"] = novo

print(Computador["memoria"])
status=input("Digite o status do equipamento: ")
Computador["status"]=status
print(Computador["status"])