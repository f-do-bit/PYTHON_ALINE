'''
#exercicio 1
listaNomes=['Fabricio', 'Matheus', 'Giovane']
'''
'''
#exercicio 2
listadenomesvazia=[]

nome1=input('Digite o primeiro nome ')
listadenomesvazia.append(nome1)

nome2=input('Digite o segundo nome ')
listadenomesvazia.append(nome2)

nome3=input('Digite o terceiro nome ')
listadenomesvazia.append(nome3)

nome4=input('Digite o quarto nome ')
listadenomesvazia.append(nome4)
#exercicio 3
listadenomesvazia.remove('Fabricio')
print(listadenomesvazia)
'''
"""
#exercicio 4

listadenomesvazia=[]
nome1=input('Digite o primeiro nome ')
listadenomesvazia.append(nome1)

nome2=input('Digite o segundo nome ')
listadenomesvazia.append(nome2)

nome3=input('Digite o terceiro nome ')
listadenomesvazia.append(nome3)

nome4=input('Digite o quarto nome ')
listadenomesvazia.append(nome4)

nome5=input('Digite o quinto nome ')
listadenomesvazia.append(nome5)
print(listadenomesvazia)
listadenomesvazia.remove(input('Coloque o nome que deseja remover '))
print(listadenomesvazia)
"""
"""
#exercicio 5
listadenumerosvazia=[]
num1=input('Digite o primeiro número ')
listadenumerosvazia.append(num1)

num2=input('Digite o segundo número ')
listadenumerosvazia.append(num2)

num3=input('Digite o terceiro número ')
listadenumerosvazia.append(num3)

num4=input('Digite o quarto número ')
listadenumerosvazia.append(num4)

num5=input('Digite o quinto número ')
listadenumerosvazia.append(num5)
print(listadenumerosvazia)
"""
#exercicio 6
produtos = ['Arroz', 'Feijao', 'Leite', 'Pao Frances', 'Ovos', 'Acucar', 'Farinha de trigo', 'Oleo De Soja', 'Tomate', 'Banana', 'Maca', 'Cafe Em Po', 'Carne Bovina',
'Peito De Frango', 'Batata', 'Cebola', 'Alface', 'Agua', 'Queijo Mussarela', 'Arroz Integral'] 
precos = [8.0, 12.5, 5.8, 10.0, 14.4, 4.5, 4.0, 7.0, 10.24, 9.72, 14.6, 18.0,
54.0, 25.0, 7.17, 6.32, 5.8, 4.0, 62.0, 10.0]

print("--- BUSCA DE PREÇO ---")
busca = input("Digite o nome do produto: ")

if busca in produtos:
    indice = produtos.index(busca)
    print(f"O preço de {busca} é: R$ {precos[indice]}")
else:
    print("Produto não encontrado.")

print("-" * 30)

precos_ordenados = sorted(precos)

menor = precos_ordenados[0]
maior = precos_ordenados[-1]

soma = (
    precos[0] + precos[1] + precos[2] + precos[3] + precos[4] + 
    precos[5] + precos[6] + precos[7] + precos[8] + precos[9] + 
    precos[10] + precos[11] + precos[12] + precos[13] + precos[14] + 
    precos[15] + precos[16] + precos[17] + precos[18] + precos[19]
)
media = soma / len(precos)

resultados = [soma, media, maior, menor]

Operacoes = ["Soma", "Média", "Maior número", "Menor número"]

print("--- RESULTADOS DOS CÁLCULOS ---")
print(f"O cálculo de {Operacoes[0]} Resultou em {resultados[0]}")
print(f"O cálculo de {Operacoes[1]} Resultou em {resultados[1]}")
print(f"O cálculo de {Operacoes[2]} Resultou em {resultados[2]}")
print(f"O cálculo de {Operacoes[3]} Resultou em {resultados[3]}")