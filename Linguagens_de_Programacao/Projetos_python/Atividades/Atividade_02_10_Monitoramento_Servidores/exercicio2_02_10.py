servidores = [ {"nome": "SRV01", "status": "Online"}, {"nome": "SRV02", "status": "Offline"}, {"nome": "SRV03", "status": "Online"}, {"nome": "SRV04", "status": "Offline"} ]

# Mostrando todos
print(servidores)

contador=0
for servidor in servidores:
    if servidor["status"]=="Online":
        print(servidor["nome"], servidor["status"])
        contador+=1

print("Existem ",contador," servidores Online")

contador2=0
for servidor in servidores:
    if servidor["status"]=="Offline":
        print(servidor["nome"], servidor["status"])
        contador2+=1

if contador2>=2:
    print("Tem ",contador2," servidores offline, ALERTA: Tem servidores em excesso")
else:
    print("Existem ",contador2," servidores offline")