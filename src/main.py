from data import disciplinas,pre_requisitos


def cria_grafo_pre_requisitos(disciplinas, pre_requisitos):
    #& inicializa grafo
    grafo = {}
    for disciplina in disciplinas:
        grafo[disciplina] = []
    #& adiciona vizinhos a cada nó
    for pre_requisito, materia in pre_requisitos:
        grafo[pre_requisito].append(materia)
    return grafo
grafo_pre_requisitos = cria_grafo_pre_requisitos(disciplinas,pre_requisitos)
print(grafo_pre_requisitos)

def dfs(grafo):
    visitados = []
    arvore = []
    for materia in grafo:
        if materia not in visitados:
            dfs_visit(grafo,materia, visitados, arvore)
    return visitados,arvore
def dfs_visit(grafo, materia, visitados, arvore):
    visitados.append(materia)
    for vizinho in grafo[materia]:
        if vizinho not in visitados:
            arvore.append((materia,vizinho))
            dfs_visit(grafo,vizinho, visitados, arvore, )

ordem_visitados, arvore_dfs = dfs(grafo_pre_requisitos)
print("ordem de visitação dfs", ordem_visitados)
print("arvore dfs", arvore_dfs)
