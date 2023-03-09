# projeto calculadora

entrada = input('Deseja calcular algo? (S/N) ')

while entrada.upper() == 'S':
    n1 = input('Digite o primeiro número: ')

    while n1.isdigit() == False:
        n1 = input('Valor inválido. Digite o primeiro número.')
    
    n2 = input('Digite o segundo número: ')

    while n2.isdigit() == False:
        n2 = input('Valor inválido. Digite o segundo número.')
    
    def operador():
        op = input('Digite o operador que deseja utilizar: (+,-,/) ')
        if op == '+':
            print(f'{n1} mais {n2} é igual a {int(n1)+int(n2)}')
        elif op == '-':
            print(f'{n1} menos {n2} é igual a {int(n1)-int(n2)}')
        elif op == '/':
            print(f'{n1} dividido por {n2} é igual a {(int(n1)/int(n2)):.2f}')
        else:
            print('Operador inexistente!')
            operador()

    operador()

    entrada = input('Deseja calcular algo novamente? (S/N) ')