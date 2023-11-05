from time import sleep

quantidade = 0

while True:
    print('-----' * 7)  # Texto informativo
    print('Validação entre dois números!')
    print('-----' * 7)
    
    # Pede ao usuário dois números para validação
    num1 = int(input('Escolha o primeiro número: '))
    num2 = int(input('Escolha o Segundo número: '))
    
    print('Aguarde um momento que estamos verificando as informações.')
    sleep(3)
    
    if num1 > num2:
        print('{} O primeiro número é maior que o segundo {}'.format(num1, num2))
    elif num2 > num1:
        print('{} O Segundo número é maior que o primeiro {}'.format(num2, num1))
    
    quantidade += 1
    
    resposta = input('Deseja fazer outra validação? (digite "sim" ou "não"): ')
    
    if resposta.lower() != 'sim':
        print('A quantidade de vezes verificadas foram: {}'.format(quantidade))
        break  # Sai do loop se a resposta não for "sim"
