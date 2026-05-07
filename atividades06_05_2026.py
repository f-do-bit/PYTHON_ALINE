"""
notaAluno=float (input('Informe sua nota'))
if notaAluno<=20:
    print('Reprovado')
elif notaAluno<=40:
    print('Recuperação 1')
elif notaAluno<50:
        print('Recuperação 2')
elif notaAluno>=50:
        print('Aprovado')
"""
"""
"""
"""
nomeAluno=input('Informe seu nome')
frequencia=float(input('informe sua nota'))
localizacaoetec=input('informe sua etec')
cursando=input('informe seu curso')
nota=input('informe sua nota')
if frequencia>=75 and localizacaoetec=='mooca' and cursando=='python' and nota>=50:
    print(f'{nomeAluno} foi aprovado')
elif frequencia>=75 and localizacaoetec=='vila alpina' and cursando=='python' and nota>=60:
    print(f'{nomeAluno} foi aprovado')
"""
"""
nota=input('informe sua nota')
if nota>=50:
    print('Você foi aprovado')
"""
"""
nota=input
if nota>=30:
    print('Você tem direito a recuperação')
"""
"""
nota=float (input('informe sua nota '))
horasCurso=float (input('informe as horas de curso '))
horaspresente=float (input('informe as horas frequentes '))
frequencia = float (horaspresente/horasCurso*100)
if frequencia >75 and nota >= 50:
    print('Voceê foi aprovado')
elif frequencia <=75 and nota <50:
    print('você foi reprovado')
elif frequencia >75 and nota <50:
    print('Você foi reprovado')
elif frequencia <=75 and nota >=50:
    print('você foi reprovado')
"""

"""
nota=float(input('Informe sua nota '))
nomeEscola=input('Informe o nome da sua escola ')
horasPresente=float(input('Informe a carga horária do curso'))
horasCurso=float(input('Informe as horas frequentadas'))
presenca=float(horasPresente/horasCurso*100)

if nota>70 and nomeEscola=='HRC' and presenca>=50:
    print('Você foi aprovado')
elif nota >=30 <=50:
    print('Você está de recuperação')
elif nota >50 <=70:
    print('Você está de exame')
elif nota>70 and presenca>=40:
    print('Você foi aprovado')
elif nota <30:
    print('Você foi reprovado')
"""
'''
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b

elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a

else:
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a

print(f"Ordem crescente: {menor}, {meio}, {maior}")
'''