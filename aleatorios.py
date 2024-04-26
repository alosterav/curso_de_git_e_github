import random


# for i in range(5):
#     print(random.randint(1,50))

# valor = random.random() #numero entre 0 e 1
# print(valor)

# print(round(random.random()*10,2)) #numero entre 0 e 10

# valor2 = random.uniform(1,100)
# print(round(valor2,4)) #um numero quebrado entre 1 e 100

lista_nums = [706, 965, 761, 321, 604, 907,
                700, 493, 29, 716, 3, 777, 807,
                136, 333, 955, 654, 252, 951,
                154]
# sorteado = random.choice(lista_nums)
# print(sorteado)

# tres_sort = random.sample(lista_nums,5)
# print(tres_sort)

print(f"lista original: {lista_nums}")

random.shuffle(lista_nums)

print(f"lista embaralhada: {lista_nums}")
