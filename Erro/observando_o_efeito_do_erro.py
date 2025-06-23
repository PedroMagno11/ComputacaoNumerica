resultado = []

def operacao(k, rep=0, max_rep=60):
    resultado.append(k)
    if rep >= max_rep:
        return
    if 0 <= k <= 0.5:
        k = k * 2
    elif 0.5 < k <= 1:
        k = k*2 - 1
    else:
        return
    operacao(k, rep+1, max_rep)


operacao(1/10)
print(resultado)