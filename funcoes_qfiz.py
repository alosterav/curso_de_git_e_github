matriculas = {"lucas vieira":123070443, "carla lima":234020334,
              "fabio almeida":123444056, "julia cardoso":213434985, }

def ver_matricula():
    """Devolve o numero de matrícula"""

    num = input("Nome completo: ")

    if num in matriculas:
        print(f"\nBEM VINDO ALUNO {num} !")
        print(f"Seu numero de matricula é: {matriculas[num]}")
    
    else:
        print(f"O {num} não está matriculado(a) ")

def add_aluno():
    """Adiciona um novo aluno"""

    parar = True
    while parar:
        parar_aux = input("Adicionar aluno? S/n ")
        if parar_aux.lower() == 'n':
            parar = False
            continue

        nome = input("nome completo: ")
        matricula = int(input("matricula: "))

        matriculas[nome] = matricula
        print(f"Aluno: {nome} matriculado")

def exc_aluno():
    """Exclui um aluno"""
    
    aluno = input("nome completo: ")
    if aluno in matriculas:
        del matriculas[aluno]
        print("Auno excluido com sucesso!")
    else:
        print("O aluno {nome} NÃO existe!")