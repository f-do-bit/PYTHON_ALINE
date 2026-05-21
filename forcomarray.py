bomdias = []
for i in range(5):
    nome = input('qual é o seu nome? \n ') #\n funciona como espaço 'pula linha' na programação
    bomdias.append(nome)
    print('bom dia {}'.format(nome))
    print(bomdias)