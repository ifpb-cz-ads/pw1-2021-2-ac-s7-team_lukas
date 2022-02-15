t = [-10, -8, 0, 1, 2, 5, -2, -4]

minima = t[0]
maxima = t[0]
soma = 0

for e in t:
    if minima > e:
        minima = e

    if maxima < e:
        maxima = e

    soma += e

media = soma / len(t)

print("{} é a menor temperatura. {} é a maior temperatura. {} é a temperatura média.".format(minima, maxima, media))