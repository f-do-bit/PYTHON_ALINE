estado=input('Informe seu estado ')
valor=float(input('informe o valor da compra '))
if estado == 'são paulo' and valor >= 100:
    print('frete gratis')
else:
    print('pagar frete')