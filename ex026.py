nome = str(input('informe a palavra: ')).lower()
print('A letra A aparece {}'.format(nome.count('a')))
print('A primeira letra A aparece na posicao {}'.format(nome.find('a')))
print('A Ultima letra A aparece {}'.format(nome.rfind('a')))