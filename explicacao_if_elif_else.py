meta = 100
vendas = input("Digite o valor das suas vendas: ")
vendas = int(vendas)

if vendas >= 2*meta:
    print ('O funcionário recebe um bônus de {}.' .format (0.2*vendas))
elif vendas >= meta:
    print ('O funcionário recebe um bônus de {}.' .format (0.1*vendas))
else:
    print('O funcionário não recebe bônus.')