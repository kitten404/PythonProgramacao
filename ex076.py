tupla = ('Maça Kg', 5.50, 'Uva Kg', 10.50, 'Banana Kg', 2.20,
         'Compota de Maçã', 8.49, 'Doce de Leite', 5.97, 'Queijo Minas', 10.92)

for i in range(0,len(tupla), 2):
    print(tupla[i],'........................... R$ ', tupla[i+1])