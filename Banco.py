from time import sleep
print('*'*20)
print('Seja bem vindo a...')
print('*'*20)

tempo = sleep(1)

print('RS Artigos Religiosos')
print('*'*7)

valor = float(input('VALOR TOTAL DE COMPRAS:R$'))

if valor >= 100:
    print('''
    Forma de pagamento:
    [1] A vista!
    [2] Boleto!
    [3] Cartão a vista!
    [4] Cartão parcelado!
    ''')
    opcao = int(input('>>> '))
    if opcao == 1:
        desconto = (valor * 10) / 100
        valor_final = valor - desconto
        print('O valor de sua compra ficou em R${:.2f}'.format(valor_final))
    if opcao == 2:
        desconto = (valor * 10) / 100
        valor_final = valor + desconto
        print('O valor de sua compra ficou em R${:.2f} em 12x de R${:.2f}'.format(valor_final, (valor_final / 12)))
    if opcao == 3:
        desconto = (valor * 5) / 100
        valor_final = valor - desconto
        print('O valor de sua compra ficou em R${:.2f}'.format(valor_final))
    if opcao == 4:
        quantas_vezes = int(input('''Quanta vezes:
        [1] 3X 
        [2] 6X
        [3] 12X
        '''))
        if quantas_vezes == 1:
            desconto = (valor * 3) / 100
            valor_final = valor + desconto
            print('O valor final ficou em R${:.2f} dividido em 3X de R${:.2f} '.format(valor_final,(valor_final / 3)))
        if quantas_vezes == 2:
            desconto = (valor * 5) / 100
            valor_final = valor + desconto
            print('O valor final ficou em R${:.2f} dividido em 3X de R${:.2f} '.format(valor_final, (valor_final / 6)))
        if quantas_vezes == 3:
            desconto = (valor * 10) / 100
            valor_final = valor + desconto
            print('O valor final ficou em R${:.2f} dividido em 3X de R${:.2f} '.format(valor_final, (valor_final / 12)))

elif valor < 100:
    print('''
        Forma de pagamento:
        [1] A vista
        [2] Cartão a vista
        [3] cartão 2x
        ''')
    opcao = int(input('Qual forma voce escolhe: '))
    if opcao == 1:
        desconto = (valor * 10) / 100
        valor_final = valor - desconto
        print('O valor de sua compra ficou em R${:.2f}'.format(valor_final))
    elif opcao == 2:
        desconto = (valor * 5) / 100
        valor_final = valor - desconto
        print('O valor de sua compra ficou em R${:.2f}'.format(valor_final))
    elif opcao ==3:
        print('O valor de sua compra ficou de {:.2f} em 2X de {:.2f }.'.format(valor,(valor/2)))
