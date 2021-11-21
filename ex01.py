cont_S = 0
cont_C = 0
cont_V = 0
cont_D = 0
cont_idade = 0
menor_20 = 0
maior_30 = 0
contmul_sol = 0
conthom_cas = 0
menor_idade = 100
maior_idade = 0

print('Digite os dados de cada pessoa: ')
print('Obs.: \nSexo = M/F \nEstado civil (S-solteiro, C-casado, V-viúvo ou D-divorciado)')
for i in range(300):
    idade = int(input('\nIdade: '))
    sexo = str(input('Sexo: ')).upper()
    civil = str(input('Estado civil: ')).upper()

    if civil == 'S':
        cont_S = cont_S + 1
    elif civil == 'C':
        cont_C = cont_C + 1
    elif civil == 'V':
        cont_V = cont_V + 1
    elif civil == 'D':
        cont_D = cont_D + 1

    if idade >= 20 and idade <= 30:
        cont_idade = cont_idade + 1

    if sexo == 'M':
        cont_sexoM = 'Masculino'
    else:
        cont_sexoF = 'Feminino'

    if sexo == 'F' and civil == 'S' and idade < 20:
        contmul_sol = contmul_sol + 1
    elif sexo == 'M' and civil == 'C' and idade > 30:
        conthom_cas = conthom_cas + 1

    if sexo == 'F' and idade < menor_idade:
        menor_idade = idade
    elif sexo == 'M' and idade > maior_idade:
        maior_idade = idade

print(f'\nSolteiros: {cont_S} \nCasados: {cont_C} \nViúvos: {cont_V} \nDivorciados: {cont_D}')
print(f'\nHá {cont_idade} pessoa(s) com idade entre 20 e 30 anos')
print(f'Há {contmul_sol} mulhere(s) solteiras com idade inferior a 20 anos')
print(f'Há {conthom_cas} homem(ns) casados com idade superior a 30 anos')
print(f'\nA maior idade dos homens é: {maior_idade}')
print(f'A menor idade das mulheres é: {menor_idade}')