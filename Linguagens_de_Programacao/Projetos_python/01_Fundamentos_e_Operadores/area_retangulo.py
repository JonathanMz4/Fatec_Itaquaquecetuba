base=float(input("Base: "))
altura=float(input("Altura: "))
if base>altura or altura>base:
    area=base*altura
    print(f"A área do retângulo é: {area}")
else:
    print("Digite valores corretos: ")