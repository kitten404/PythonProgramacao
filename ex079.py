sair = "N"
numbers = list()
while sair in "Nn" :
    numbers.append(int(input("Digite um valor:  ")))
    sair = str(input("Deseja sair ? [S/N] "))

numbers.sort()
print("Os numeros digitados foram {}".format(numbers))