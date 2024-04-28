# FUNÇÕES LAMBDA (ANÔNIMAS)

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x%2 == 0

# print(par(4))

# f_c = lambda f: (f - 32) * 5/9

# print(f_c(32))

# num = [1,2,3,4,5,6,7,8]
# dobro = map(lambda x:x**2, num)
# print(list(dobro))

# palavras = ["a","vida","não","é","um","jogo"]
# maiusculas = map(str.  upper,palavras)
# print(list(maiusculas))

#num = [1,3,4,5,6,7,8,9,44,332,2,78,6,7,0,98,21]

# def pares(n):
#     return n % 2 == 0

# num_par = filter(pares,num)
# print(list(num_par))

# num_impar = filter(lambda x: x%2 != 0, num)
# print(list(num_impar))

# num = [1,3,4,5,6,7,8,9,44]

from functools import reduce

# def mult(x,y):
#     return x*y

# total = reduce(mult, num)
# print(total)

# num = [1,2,3,4]
 
# total = reduce(lambda x,y: x**2+y**2, num)
# print(total)