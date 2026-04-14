disciplinas = [
    # 1º Semestre
    "Cálculo 1", "APC", "DIAC", "Engenharia e Ambiente", "Introdução à Engenharia",
    # 2º Semestre
    "Cálculo 2", "Física 1", "Física 1 Experimental", "IAL", "Probabilidade e Estatística", "Desenvolvimento de Software",
    # 3º Semestre
    "Métodos Numéricos", "Engenharia Econômica", "Humanidades e Cidadania", "TED 1", "PED 1", "OO", "MD 1",
    # 4º Semestre
    "Gestão de Produção e Qualidade", "MDS", "EDA 1", "FAC", "MD 2", "PI 1",
    # 5º Semestre
    "IHC", "Requisitos", "SBD 1", "FSO", "Compiladores 1", "EDA 2",
    # 6º Semestre
    "Qualidade de Software 1", "Testes de Software", "ADS", "Redes", "SBD 2", "PAA",
    # 7º Semestre
    "TPPE", "Paradigmas de Programação", "FSE", "Programação Paralela e Distribuída",
    # 8º Semestre
    "Engenharia de Produto", "GCES",
    # Finais
    "TCC 1", "TCC 2", "PI 2"
]

pre_requisitos = [
    # 1º -> 2º Semestre
    ("Cálculo 1", "Cálculo 2"),
    ("Cálculo 1", "Probabilidade e Estatística"),
    ("APC", "Desenvolvimento de Software"),
    
    # 2º -> 3º Semestre
    ("Cálculo 2", "Métodos Numéricos"),
    ("IAL", "TED 1"),
    ("IAL", "PED 1"),
    ("APC", "OO"),
    
    # 3º -> 4º Semestre
    ("Engenharia Econômica", "Gestão de Produção e Qualidade"),
    ("OO", "MDS"),
    ("APC", "EDA 1"),
    ("TED 1", "FAC"),
    ("PED 1", "FAC"),
    ("MD 1", "MD 2"),
    
    # 4º -> 5º Semestre
    ("MDS", "IHC"),
    ("MDS", "Requisitos"),
    ("EDA 1", "Compiladores 1"),
    ("FAC", "FSO"),
    ("MD 2", "SBD 1"),
    ("EDA 1", "EDA 2"),
    
    # 5º -> 6º Semestre
    ("Requisitos", "ADS"),
    ("IHC", "Qualidade de Software 1"),
    ("Gestão de Produção e Qualidade", "Qualidade de Software 1"),
    ("Requisitos" ,"Testes de Software"),
    ("MDS" ,"Testes de Software"),
    ("SBD 1", "SBD 2"),
    ("FSO", "Redes"),
    ("EDA 1", "PAA"),
    
    # 6º -> 7º Semestre
    ("Testes de Software", "TPPE"),
    ("ADS", "TPPE"),
    ("OO", "Paradigmas de Programação"),
    ("Compiladores", "Paradigmas de Programação"),
    ("FSO", "FSE"),
    ("Redes", "Programação Paralela e Distribuída"),
    ("EDA 2", "Programação Paralela e Distribuída"),
    
    # 7º -> 8º Semestre
    ("TPPE", "Engenharia de Produto"),
    ("Testes de Software", "GCES"),
    
    # TCCs e Projetos Integradores
    ("PI 1", "PI 2"),
    ("TCC 1", "TCC 2")
]

for pre_requisito, materia in pre_requisitos:
    if pre_requisito not in disciplinas:
        raise Exception(f"Erro: {pre_requisito} não está na lista de disciplinas.")
    if materia not in disciplinas:
        raise Exception(f"Erro: {materia} não está na lista de disciplinas.")
                

def imprimeDados():
    print(f"Total de Disciplinas: {len(disciplinas)}")
    print(f"Total de Dependências: {len(pre_requisitos)}")
    print("\n--- Relações de Pré-Requisito ---")
    for pre, mat in pre_requisitos:
        print(f"[{pre}] -> [{mat}]")

if __name__ == "__main__":
    imprimeDados()
