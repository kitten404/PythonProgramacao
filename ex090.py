pessoas = {'nome':'Quezia', 'idade':25, 'sexo':'F'}
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print('{0} tem {1} anos'.format(pessoas['nome'],pessoas['idade']))
print(pessoas.items())

brasil =[]
estado = {'uf':'Sao Paulo','sigla':'SP'}
estado1 = {'uf':'Minas Gerais','sigla':'MG'}

brasil.append(estado)
brasil.append(estado1)

for k in brasil:
    for c in k.values():
        print(c)


aluno = dict()
aluno['nome'] = str(input('Qual o nome?: '))
aluno['media'] = float(input('Qual a media de {}: '.format(aluno['nome'])))
if(aluno['media'] >= 6):
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for c,v in aluno.items():
    print(c,' é igual ', v)


