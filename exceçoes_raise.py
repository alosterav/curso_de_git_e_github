from math import sqrt

class NegativeNumberError(Exception): #criando uma exception
    def __init__(self):
        pass

if __name__ == "__main__":
    try:
        num = int(input("Entre com um numero: "))
        if num < 0:
            raise NegativeNumberError #usando a exception criada
        
    except NegativeNumberError: #usando a exception criada
        print("Não pode número negativo!")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print(f"Fim do cálculo")