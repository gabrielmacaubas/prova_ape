flag = 0
matricula = int(input("Matrícula: "))
soma_salario_bruto = float()
soma_desconto_inss = float()
soma_salario_liquido = float()
contagem_funcionarios = int()
maior_salario = int()

while matricula != flag:
    nome = str(input("Nome: "))
    salario_bruto = float(input("Salário bruto: R$ "))
    desconto_inss = (salario_bruto * 12) / 100
    salario_liquido = salario_bruto - desconto_inss
    contagem_funcionarios += 1

    if salario_liquido > maior_salario:
        maior_matricula = matricula
        maior_salario = salario_liquido
        maior_funcionario = nome

    # Área de Formatação
    # Condições para declarar o espaçamento entre as strings
    if len(nome) < 4:
        nome_tamanho = 7

    else:
        nome_tamanho = len(nome) + 3

    # Declarando a variável texto para medir tamanho e executar linha de traços ao final
    texto = f"\n{'Matrícula':<12}{'Nome':<{nome_tamanho}}{'Salário Bruto':<16}{'Desconto INSS':<16}{'Salário Líquido'}"

    print(texto)
    print(
        f"{matricula:<12}{nome:<{nome_tamanho}}R$ {salario_bruto:<13.2f}R$ {desconto_inss:<13.2f}R$ {salario_liquido:.2f}")
    print(len(texto) * "-")

    soma_salario_bruto += salario_bruto
    soma_desconto_inss += desconto_inss
    soma_salario_liquido += salario_liquido

    matricula = int(input("\nMatrícula: "))

media_salarial = soma_salario_liquido / contagem_funcionarios

print(f"\n{'RESULTADO':-^30}")
print(
    f"\nSalários brutos: R$ {soma_salario_bruto:.2f}\nDescontos INSS: R$ {soma_desconto_inss:.2f}\nSalários Líquidos: R$ {soma_salario_liquido:.2f}")
print(f"Média Salarial: R${media_salarial:.2f}")
print(f"\n{'MELHOR FUNCIONÁRIO':-^30}")
print(f"\nMatrícula: {maior_matricula}")
print(f"Nome: {maior_funcionario}")
print(f"Salário: R${maior_salario:.2f}")
