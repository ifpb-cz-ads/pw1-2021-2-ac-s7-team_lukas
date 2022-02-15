pilha = []
erro = False

expresao= input("Digite a expressão a ser verificada: ")

for item in expresao:
    if item == '(':
        pilha.append(item)
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            erro = True

if len(pilha) == 0 and not erro:
    print('A expressão está correta')
else:
    print("Erro, a expressão contém caracteres incorretos")