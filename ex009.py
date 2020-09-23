import math
n1 = int(input('Digite o valor para exibir a tabuada: '))
aux = 1
while(aux<=10) :
    print('{0} x {1} = {2}'.format(n1,aux,n1*aux))
    aux=aux+1