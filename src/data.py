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
    ("APC", "Desenvolvimento de Software"),
    
    # 2º -> 3º Semestre
    ("Cálculo 2", "Métodos Numéricos"),
    ("IAL", "TED 1"),
    ("Desenvolvimento de Software", "OO"),
    
    # 3º -> 4º Semestre
    ("TED 1", "PED 1"),
    ("OO", "MDS"),
    ("OO", "EDA 1"),
    ("MD 1", "MD 2"),
    ("MD 1", "EDA 1"),
    ("PED 1", "FAC"),
    
    # 4º -> 5º Semestre
    ("MDS", "Requisitos"),
    ("EDA 1", "SBD 1"),
    ("EDA 1", "EDA 2"),
    ("FAC", "FSO"),
    ("MD 2", "Compiladores 1"),
    ("PI 1", "FSO"),
    
    # 5º -> 6º Semestre
    ("Requisitos", "ADS"),
    ("Requisitos", "Qualidade de Software 1"),
    ("SBD 1", "SBD 2"),
    ("FSO", "Redes"),
    ("EDA 2", "PAA"),
    ("Compiladores 1", "PAA"),
    
    # 6º -> 7º Semestre
    ("Qualidade de Software 1", "TPPE"),
    ("ADS", "TPPE"),
    ("PAA", "Paradigmas de Programação"),
    ("FSO", "FSE"),
    ("Redes", "Programação Paralela e Distribuída"),
    
    # 7º -> 8º Semestre
    ("TPPE", "Engenharia de Produto"),
    ("TPPE", "GCES"),
    
    # TCCs e Projetos Integradores
    ("PI 1", "PI 2"),
    ("TCC 1", "TCC 2")
]

for pre_requisito, materia in pre_requisitos:
    if pre_requisito not in disciplinas:
        raise Exception(f"Pré-requisito inválido: {pre_requisito}, verificar disciplinas")
    if materia not in disciplinas:
        raise Exception(f"Matéria inválida: {materia}, verificar discplinas")
                

def imprimeDados():
    print("Disciplinas")
    for disciplina in disciplinas:
        print("-",disciplina)
    print("\nPré Requisitos")
    for pre_requisito, materia in pre_requisitos:
        print(f"{pre_requisito} é pré-requisito de {materia} ")
if __name__ == "__main__":
    imprimeDados()
