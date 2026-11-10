idade = int(input("Digite sua idade: "))
nota = float(input("Digite sua nota: "))

maioridade=idade>=18
nota_minima=nota>=6
print(maioridade)
print(nota_minima)
print(maioridade and nota_minima)

# Os valores impressos serão true ou false e vai variar de acordo com a idade e nota 

# O último só vai funcionar se os dois forem verdadeiros