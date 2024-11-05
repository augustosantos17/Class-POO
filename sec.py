placas = ['ABC-1234', 'DEF-4567', 'CDE-4321', 'WXY-2121', 'AAA-1112']
precos = [2500000, 7000000, 5000000, 2000000, 8000000]
marcas = ['Pagani', 'Ferrari', 'Porsche', 'BMW', 'Lamborghini']
modelos = ['Zonda R', '812 competizione', '911 GT3 RS', 'M3 Competition', 'Aventador SVJ']

print("Dados cadastrados: ")
print(placas,"\n", precos, "\n", marcas,"\n", modelos, "\n")

soma= 0
qtde = 0
mpesq = input("Digite uma marca para pesquisar: ")
for i in range(len(placas)):
    if(marcas[i] ==mpesq) :
        soma += precos[i]
        qtde = qtde + 1
    
print("A média de preço dos carros da marca", mpesq, "é", soma/qtde, "\n")

print("Carros com preço abaixo de R$55.000,00: ")
for i in range (len(placas)):
    if(precos[i] < 55000000):
        print(placas[i], precos[i], marcas[i], modelos[i])


menor = 999999999
pos = -1
for i in range (len(placas)):
    if (precos [i] < menor):
        menor = precos [i]
        pos = i
    
print("O carro mais barato é: ", placas[pos], "R$", precos[pos], marcas[pos], modelos[pos])