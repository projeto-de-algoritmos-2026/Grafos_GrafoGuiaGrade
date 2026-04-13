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

def obter_scc(grafo):
    """Implementa o Algoritmo de Kosaraju para encontrar SCCs."""
    # Passo 1: Obter a ordem de finalização (usando sua lógica de ordenação topológica)
    # Aqui, mesmo com ciclo, precisamos da ordem de término da DFS
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

    # Passo 2: Transpor o grafo
    grafo_t = transpor_grafo(grafo)

    # Passo 3: DFS no grafo transposto seguindo a pilha invertida
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

# --- Testando no seu fluxo ---
print("\n--- Componentes Fortemente Conectados (SCC) ---")
sccs = obter_scc(grafo_pre_requisitos)
for i, scc in enumerate(sccs):
    print(f"SCC {i+1}: {scc}")


# def ordenacao_topologica_kahn(grafo, pre_requisitos):
#     grau_entrada = {disciplina: 0 for disciplina in grafo}

#     for pre_requisito, materia in pre_requisitos:
#         grau_entrada[materia] += 1

#     print("Graus iniciais:", grau_entrada)

#     fila = [materia for materia in grau_entrada if grau_entrada[materia] == 0]
#     print("Fila inicial:", fila)

#     ordem = []

#     while fila:
#         atual = fila.pop(0)
#         print(f"\nProcessando: {atual}")

#         ordem.append(atual)

#         for vizinho in grafo[atual]:
#             grau_entrada[vizinho] -= 1
#             print(f"Atualizando {vizinho}: grau = {grau_entrada[vizinho]}")

#             if grau_entrada[vizinho] == 0:
#                 print(f"{vizinho} entrou na fila")
#                 fila.append(vizinho)

#     print("\nOrdem final:", ordem)

#     if len(ordem) != len(grafo):
#         raise Exception("Ciclo detectado!")

#     return ordem

# print(ordenacao_topologica_kahn(grafo_pre_requisitos, pre_requisitos))