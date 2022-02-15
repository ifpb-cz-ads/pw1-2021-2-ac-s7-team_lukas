L = [15, 7, 27, 39]

p = int(input("Digite o primeiro valor a ser procurado: "))
v = int(input("Digite o segundo valor a ser procurado: "))
achou = ""

x = 0
while x < len(L):
    if L[x] == p:
        achou = "p"
        break
    elif L[x] == v:
        achou = "v"
        break
    x += 1

if achou == "p":
    print("%d achado na posição %d" % (p,x))
elif achou == "v":
    print("%d achado na posição %d" % (v,x))
else:
    print("%d e %d não encontrados" % (p, v))