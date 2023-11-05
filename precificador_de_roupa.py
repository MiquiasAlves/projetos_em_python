from time import sleep
while True:
    #Texto Informativo
    print('---------' * 5)
    print('Precificação de Produtos')
    print('---------' * 5)
    print('Escolha uma opção:')
    print('[1] Camiseta')
    print('[2] Calça')
    print('[3] Vestido')
    print('[4] Encerrar sessão')
    #Pergunta a opção ao opção ao usuário
    print('---------' * 5)
    resposta = int(input('Sua escolha é: '))
    print('---------' * 5)

    
    if resposta == 1:
        print('---------' * 5)
        print('Você escolheu a opção camiseta.')
        print('---------' * 5)
        valor_de_compra_camiseta = float(input('Qual o valor de compra do produto: R$ '))
        valor_de_custo_camiseta = valor_de_compra_camiseta + (valor_de_compra_camiseta * 0.20)
        valor_com_lucro_camiseta = valor_de_custo_camiseta + (valor_de_custo_camiseta * 0.75)
        print('O valor de venda deste produto é R$ {:.2f}'.format(valor_com_lucro_camiseta))
    elif resposta == 2:
        print('---------' * 5)
        print('Você escolheu a opção Calça.')
        print('---------' * 5)
        valor_de_compra_calça = float(input('Qual o valor de compra do produto: R$ '))
        valor_de_custo_calça = valor_de_compra_calça + (valor_de_compra_calça * 0.20)
        valor_com_lucro_calça = valor_de_custo_calça + (valor_de_custo_calça * 1.00)
        print('O valor de venda deste produto é R$ {:.2f}'.format(valor_com_lucro_calça))
    elif resposta == 3:
        print('---------' * 5)
        print('Você escolheu a opção Vestido.')
        print('---------' * 5)
        valor_de_compra_vestido = float(input('Qual o valor de compra do produto: R$ '))
        valor_de_custo_vestido = valor_de_compra_vestido + (valor_de_compra_vestido * 0.20)
        valor_com_lucro_vestido = valor_de_custo_vestido + (valor_de_custo_vestido * 0.80)
        print('O valor de venda deste produto é R$ {:.2f}'.format(valor_com_lucro_vestido))
    elif resposta == 4:
        print('Encerrando a sua sessão')
        sleep(3)
        print('Sessão encerrada')
        break
    else:
        print('Opção inválida. Por favor, escolha um opção válida')