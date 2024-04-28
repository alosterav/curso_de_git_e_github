var_global = "Curso python completo"

def escreve_texto():
    global var_global
    var_global = "Banco de dados"
    var_local = "Fabio reis"

    print(var_global)

escreve_texto()