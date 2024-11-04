lista = [4.0, 9.2, 3.1, 9.1, 1.5, 3.2, 2.6]

print("A lista é criada é ", lista)

print("O 1º elemento da lista é ", lista[0])

print("o último elemento da lista é ", lista[len(lista)-1])

soma = 0 
for i in range (len(lista)):

    soma += lista[i]

print("A soma dos elementos da lista é ", soma)

print("os elementos nas posições pares da lista são: ")

for i in range (0,len(lista),2):

    print(lista[i])