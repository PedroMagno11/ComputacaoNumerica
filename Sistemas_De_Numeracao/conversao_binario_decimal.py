def converter(binario:str)->int:
    if not binario or any(c not in '01' for c in binario):
        raise ValueError('Binário inválido: deve conter apenas "0" e "1" e não pode estar vazio')
    if len(binario)==1:
        return int(binario)
    else:
        return int(binario[0]) * (2**(len(binario)-1)) + converter(binario[1:])


while True:
    binario = input('Digite um numero binario: ')
    print(f'({binario}) na base 2 = ({converter(binario)}) na base 10')