def converter_decimal_para_binario(decimal: int) -> str:
    if decimal < 2:
        return str(decimal)
    else:
        return converter_decimal_para_binario(decimal//2) + str(decimal%2)


while True:
    decimal = int(input("Insira um número decimal: "))
    print(f'({decimal}) na base 10 = ({converter_decimal_para_binario(decimal)}) na base 2')


