n = int(input('digite o numero: '))
fatorial = 1
c = 1
while n != 0:
    fatorial = fatorial * n
    print('{0} x {1} = {2}'.format(n,c,fatorial))
    n = n -1