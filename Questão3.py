lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = []

for i in lista1:
    if i not in lista3:
        lista3.append(i)
        for x in lista2:
            if x not in lista3:
                lista3.append(x)

print('A lista resultante é: ', lista3)