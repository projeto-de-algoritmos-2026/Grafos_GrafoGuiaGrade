from data import disciplinas,pre_requisitos


def cria_grafo(disciplinas, pre_requisitos):
    #& inicializa grafo
    grafo = {}
    for disciplina in disciplinas:
        grafo[disciplina] = []
    #& adiciona vizinhos a cada nó
    for pre_requisito, materia in pre_requisitos:
        grafo[pre_requisito].append(materia)
    return grafo
grafo = cria_grafo(disciplinas,pre_requisitos)
print(grafo)