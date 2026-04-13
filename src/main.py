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
    
    for materia in grafo:
        if estados[materia] == "não visitado":
            if detectar_ciclo_visit(grafo,materia,estados):
                return True
    
    return False

def detectar_ciclo_visit(grafo,materia,estados):
    estados[materia] = "visitando"
    
    for vizinho in grafo[materia]:
        if estados[vizinho] == "visitando":
            return True
        if estados[vizinho] == "não visitado":
            if detectar_ciclo_visit(grafo,vizinho,estados):
                return True
        
    estados[materia] = "visitado"
    return False

tem_ciclo = detectar_ciclo(grafo_pre_requisitos)
print(tem_ciclo)

def ordenacao_topologica(grafo):
    if detectar_ciclo(grafo):
        raise Exception("Ciclo detectado, Grafo não é Acíclico")
    visitados = set()
    ordem = []
    for materia in grafo:
        if materia not in visitados:
            ordenacao_topologica_visit(grafo, materia, visitados, ordem)
    ordem.reverse()
    return ordem

def ordenacao_topologica_visit(grafo, materia, visitados, ordem):
    visitados.add(materia)
    for vizinho in grafo[materia]:
        if vizinho not in visitados:
            ordenacao_topologica_visit(grafo, vizinho, visitados, ordem)
    ordem.append(materia)

ordem_topologica = ordenacao_topologica(grafo_pre_requisitos)
print(ordem_topologica)

def transpor_grafo(grafo):
    """Inverte a direção de todas as arestas do grafo."""
    grafo_transposto = {disciplina: [] for disciplina in grafo}
    for u in grafo:
        for v in grafo[u]:
            grafo_transposto[v].append(u)
    return grafo_transposto


def mostrar_arvore_pre_requisitos(materia, grafo, nivel=0):
    """Exibe os pré-requisitos em formato de árvore visual."""
    prefixo = "    " * nivel + "|-- " if nivel > 0 else ""
    print(f"{prefixo}{materia}")
    
    for disciplina, sucessores in grafo.items():
        if materia in sucessores:
            mostrar_arvore_pre_requisitos(disciplina, grafo, nivel + 1)


print("\nESTRUTURA HIERÁRQUICA DE DEPENDÊNCIAS:")
mostrar_arvore_pre_requisitos("MDS", grafo_pre_requisitos)

def obter_scc(grafo):
    """Implementa o Algoritmo de Kosaraju para encontrar SCCs."""
    visitados = set()
    pilha = []

    def preencher_pilha(u):
        visitados.add(u)
        for v in grafo[u]:
            if v not in visitados:
                preencher_pilha(v)
        pilha.append(u)

    for disciplina in grafo:
        if disciplina not in visitados:
            preencher_pilha(disciplina)

    
    grafo_t = transpor_grafo(grafo)
    visitados.clear()
    sccs = []

    def dfs_scc(u, componente):
        visitados.add(u)
        componente.append(u)
        for v in grafo_t[u]:
            if v not in visitados:
                dfs_scc(v, componente)

    while pilha:
        u = pilha.pop()
        if u not in visitados:
            componente_atual = []
            dfs_scc(u, componente_atual)
            sccs.append(componente_atual)
    
    return sccs

    
if __name__ == "__main__":
    
    print("\nAbrindo interface gráfica...")
    from interface import abrir_interface
    abrir_interface(disciplinas, grafo_pre_requisitos)

