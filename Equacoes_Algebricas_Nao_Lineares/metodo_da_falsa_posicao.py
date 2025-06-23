import numpy as np

def f1(x):
    h = np.cos(x) - 3 + np.exp(x)
    return h

def f2(x):
    f = x**2 + np.log(x)
    return f

# método da falsa posicao
def falsa_posicao(a,b, tol, funcao):
    x = (a*funcao(b) - b*funcao(a))/(funcao(b)-funcao(a))
    iter = 0
    while abs(funcao(x))>tol:
        print(f'Iteracao: {iter}')
        print(f'a: {a}')
        print(f'b: {b}')
        print(f'x: {x}')
        print(f'f(x): {funcao(x)}\n')
        print('--------------------')

        if funcao(a)*funcao(x)<0 :
            a = a
            b = x

        elif funcao(x)*funcao(b)<0:
            a = x
            b = b

        x = (a * funcao(b) - b * funcao(a))/(funcao(b)-funcao(a))
        iter += 1

    print(f'A raiz da função é: {x}')
    print(f'Total de iteracao: {iter}')

falsa_posicao(0.5,1,0.5e-1, funcao=f2)