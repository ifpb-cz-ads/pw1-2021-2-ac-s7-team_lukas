A = []
B = []
x = int(input("Digite quantos numeros deseja digitar:"))
n = 0

while n < x :
    A.append(int(input("Digite um numero:")))
    n+=1

n = 0

while n < x :
    B.append(int(input("Digite um numero:")))
    n+=1

C = [A+B]

print("A lista formada com a junção das anteriores:")
print(*C , end= " ")