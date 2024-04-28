elementos = {
     'Z': 3,
     'nome': 'Lítio',
     'grupo': 'Metais Alcalins',
     'densidade':0.534,
}

# print(f"Elemento: {elementos['nome']}")
# print(f"O dicionario possui: {len(elementos)} elementos")

# elementos['grupo'] = 'Alcalinos'
# print(elementos)

# elementos['periodo'] = 1
# print(elementos)
# del elementos['periodo']
# print(elementos)
# elementos.clear()
# print(elementos)
# del elementos
# print(elementos)

# print(elementos.items())

# for i in elementos.items():
#     print(i)

# for key in elementos.keys():
#     print(key)

# for value in elementos.values():
#     print(value)

for key,value in enumerate(elementos):
    print(f"chave: {key} - Valor: {value}")