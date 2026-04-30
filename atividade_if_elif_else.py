metaFuncionario=15000
metaEmpresa=200000
vendasFuncionario=input('Insira suas vendas: ')
vendasFuncionario=float(vendasFuncionario)
vendasEmpresa=input('Insira as vendas da empresa: ')
vendasEmpresa=float(vendasEmpresa)
if vendasFuncionario >= 15000 and vendasEmpresa>=200000:
    print(f"O funcionario recebeu o bônus de {0.10*metaFuncionario}")
elif vendasFuncionario >=2*metaFuncionario and vendasEmpresa >=200000:
    print(f"O funcionário recebeu o bônus de {0.20*metaFuncionario}")
else:
    print("O funcionário não recebeu bônus")