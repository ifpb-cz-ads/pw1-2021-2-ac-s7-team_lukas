L = [15, 7, 27, 39]
posicao_p = None
posicao_v = None
x = 0

p = int(input("Digite o primeiro valor a ser procurado: "))
v = int(input("Digite o segundo valor a ser procurado: "))

while x < len(L):
    if L[x] == p:
        posicao_p = x
    elif L[x] == v:
        posicao_v = x
    x += 1

if not posicao_v is None and not posicao_p is None:
    print("%d achado na posição %d e %d achado na posição %d" % (p, posicao_p, v, posicao_v))
elif not posicao_v is None:
    print("%d achado na posição %d e %d não encontrado" % (v, posicao_v, p))
elif not posicao_p is None:
    print("%d achado na posição %d e %d não encontrado" % (p, posicao_p, v))
else:
    print("%d e %d não foram encontrados" % (p, v))