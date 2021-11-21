#declarando variaveis necessarias durante o codigo e realizando a primeira leitura de matricula
flag = 0
matricula = int(input("Matrícula: "))
soma_salario_bruto = float()
soma_desconto_inss = float()
soma_salario_liquido = float()
contagem_funcionarios = int()
maior_salario = int()

#inciando loop
while matricula != flag:
    #lendo variaveis digitadas pelo usuario
    nome = str(input("Nome: "))
    salario_bruto = float(input("Salário bruto: R$ "))

    #calculando desconto, salario liquido e contagem de funcionarios para, ao final, realizar o calculo da media salarial
    desconto_inss = (salario_bruto * 12) / 100
    salario_liquido = salario_bruto - desconto_inss
    contagem_funcionarios += 1

    #condicao para calcular salario do maior funcionario e quardar o respectivo nome e matricula caso ele seja o mais bem pago
    if salario_liquido > maior_salario:
        maior_matricula = matricula
        maior_salario = salario_liquido
        maior_funcionario = nome

    #imprimindo dados a respeito do ultimo funcionario informado
    print(f"\nMatrícula: {matricula}\nNome: {nome}\nSalário Bruto: R$ {salario_bruto:.2f}\nDesconto INSS: R$ {desconto_inss:.2f}\nSalário Líquido: R${salario_liquido:.2f}")

    #calculando variaveis necessarias para o resultado da questao envolvendo o quadro geral da empresa
    soma_salario_bruto += salario_bruto
    soma_desconto_inss += desconto_inss
    soma_salario_liquido += salario_liquido

    #recomeçando o loop
    matricula = int(input("\nMatrícula: "))

#calculando media salarial da empresa
media_salarial = soma_salario_liquido / contagem_funcionarios

#imprimindo resultados da questao (informaçoes sobre a empresa e melhor funcionario)
print("\nResultado -->")
print(f"Salários brutos: R$ {soma_salario_bruto:.2f}\nDescontos INSS: R$ {soma_desconto_inss:.2f}\nSalários Líquidos: R$ {soma_salario_liquido:.2f}")
print(f"Média Salarial: R${media_salarial:.2f}")
print(f"\n{'MELHOR FUNCIONÁRIO -->'}")
print(f"Matrícula: {maior_matricula}")
print(f"Nome: {maior_funcionario}")
print(f"Salário: R${maior_salario:.2f}")
