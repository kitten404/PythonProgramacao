km = int(input('Digite a velocidade em KM'))
if(km > 80):
    km = km - 80
    print('Multa {0}, km a mais {1}'.format(km * 7.00,km))
print('Tudo certo aqui')
