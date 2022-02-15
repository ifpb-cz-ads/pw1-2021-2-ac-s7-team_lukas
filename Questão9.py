text = input("Digite a frase a ser analisada: ").replace(" ", "")
dicionario = {}

for i in text:
    if i in dicionario:
        dicionario[i]= dicionario[i]+1
    else:
        dicionario[i] = 1
print(dicionario)