import random
jogadores = dict()
listaPlayers = list()
lista = ['Celia', 'Juliana', 'Carlos','Francisco']
for c in range(0,4):
    jogadores = {'Jogador': lista[c], 'dado': random.randint(1,6)}
    print('O Jogador',c, 'tirou', jogadores['dado'],'no dado.')
    listaPlayers.append(jogadores)

print(listaPlayers)

