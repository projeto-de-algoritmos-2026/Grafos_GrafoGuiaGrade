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

def detectar_ciclo(grafo):
    estados = {}
    for materia in grafo:
        estados[materia] = "não visitado"
    # print("estado inicial: ",estados)
    for materia in grafo:
        if estados[materia] == "não visitado":
            if detectar_ciclo_visit(grafo,materia,estados):
                return True
    # print("estado final: ",estados)
    return False

def detectar_ciclo_visit(grafo,materia,estados):
    estados[materia] = "visitando"
    # print(f"estado no loop na materia {materia}: {estados}")
    for vizinho in grafo[materia]:
        if estados[vizinho] == "visitando":
            return True
        if estados[vizinho] == "não visitado":
            if detectar_ciclo_visit(grafo,vizinho,estados):
                return True
        # print(f"estado no loop no vizinho {vizinho}: {estados}")
    estados[materia] = "visitado"
    return False

tem_ciclo = detectar_ciclo(grafo_pre_requisitos)
print(tem_ciclo)