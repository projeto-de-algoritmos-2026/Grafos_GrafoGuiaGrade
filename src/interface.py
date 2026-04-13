import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

# Cole a função aqui para evitar a importação circular
def buscar_todos_pre_requisitos(materia_alvo, grafo, visitados=None):
    if visitados is None:
        visitados = set()
    pre_requisitos_encontrados = set()
    for disciplina, sucessores in grafo.items():
        if materia_alvo in sucessores:
            pre_requisitos_encontrados.add(disciplina)
            if disciplina not in visitados:
                visitados.add(disciplina)
                ancestrais = buscar_todos_pre_requisitos(disciplina, grafo, visitados)
                pre_requisitos_encontrados.update(ancestrais)
    return pre_requisitos_encontrados

def abrir_interface(disciplinas, grafo):
    janela = tk.Tk()
    janela.title("Guia de Matérias - Engenharia de Software")
    janela.geometry("400x450")

    label = tk.Label(janela, text="Selecione uma disciplina para ver os pré-requisitos:", pady=10)
    label.pack()

    # Criar uma lista com barra de rolagem
    frame = tk.Frame(janela)
    frame.pack()
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=15)
    for d in sorted(disciplinas):
        listbox.insert(tk.END, d)
    listbox.pack()
    scrollbar.config(command=listbox.yview)

    def mostrar_info():
        selecao = listbox.curselection()
        if not selecao:
            return
        
        materia = listbox.get(selecao[0])
        # Usando sua função de busca
        pres = buscar_todos_pre_requisitos(materia, grafo)
        
        texto = f"Pré-requisitos para {materia}:\n\n"
        if pres:
            texto += "\n".join([f"• {p}" for p in sorted(pres)])
        else:
            texto += "Nenhum pré-requisito necessário."
        
        messagebox.showinfo("Dependências", texto)

    btn = tk.Button(janela, text="Ver Pré-requisitos", command=mostrar_info, bg="#4CAF50", fg="white", pady=5)
    btn.pack(pady=20)

    janela.mainloop()



# Para rodar:
# abrir_interface(disciplinas, grafo_pre_requisitos)