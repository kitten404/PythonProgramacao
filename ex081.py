sair = "N"
numbers = list()
while sair in "Nn" :
    numbers.append(int(input("Digite um valor:  ")))
    sair = str(input("Deseja sair ? [S/N] "))
print("Foram digitados {} numeros".format(len(numbers)))
numbers.sort(reverse=True)
print("Os numeros em ordem decrescente")
if (5 in numbers):
    print("o numero 5 tá na lista")
else:
    print("O numero 5 não esta na lista")