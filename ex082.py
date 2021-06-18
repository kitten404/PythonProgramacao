sair = "N"
value = 0
numbers = list()
par = list()
impar = list()
while sair in "Nn" :
    value  = int(input("Digite um valor:  "))
    numbers.append(value)
    if(value % 2 == 0):
        par.append(value)
    if(value % 2 == 1 ):
        impar.append(value)
    sair = str(input("Deseja sair ? [S/N] "))
print("Mostrando as 3 listas: Impar {0}, Par {1}, Lista {2}".format(impar,par,numbers))

