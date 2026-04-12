disciplinas = [
    "APC",
    "EDA 1",
    "EDA 2",
    "P.A"
]

pre_requisitos = [
#~ ("Pré Requisito", "Matéria"),
    ("APC","EDA 1"),
    ("EDA 1","P.A"),
    ("EDA 1","EDA 2"),
    # ("EDA 2", "APC") teste de ciclo
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
