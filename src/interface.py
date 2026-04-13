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
    janela.title("Grade Curricular - UnB FGA")
    janela.geometry("600x700")
    
    # --- PALETA DE CORES ---
    COR_FUNDO = "#1e1e2e"      # Azul escuro quase preto
    COR_CARD = "#2b2b3b"       # Cinza azulado para áreas de destaque
    COR_TEXTO = "#eff1f5"      # Branco off-white
    COR_ACENTO = "#89b4fa"     # Azul claro para botões e detalhes
    COR_DESTAQUE = "#f9e2af"   # Amarelo suave para títulos
    
    janela.configure(bg=COR_FUNDO)

    # Título Principal
    titulo = tk.Label(
        janela, 
        text="Fluxograma de Engenharia", 
        font=("Segoe UI", 18, "bold"),
        bg=COR_FUNDO, 
        fg=COR_DESTAQUE,
        pady=20
    )
    titulo.pack()

    # Instrução
    instrucao = tk.Label(
        janela, 
        text="Selecione uma matéria para analisar a árvore de dependências:",
        font=("Segoe UI", 10),
        bg=COR_FUNDO, 
        fg=COR_TEXTO
    )
    instrucao.pack(pady=5)

    # Frame Central (para organizar a lista e o texto)
    frame_central = tk.Frame(janela, bg=COR_FUNDO)
    frame_central.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    # Listbox Customizada
    listbox = tk.Listbox(
        frame_central, 
        bg=COR_CARD, 
        fg=COR_TEXTO, 
        font=("Segoe UI", 11),
        selectbackground=COR_ACENTO,
        selectforeground=COR_FUNDO,
        borderwidth=0,
        highlightthickness=1,
        highlightcolor=COR_ACENTO
    )
    for d in sorted(disciplinas):
        listbox.insert(tk.END, d)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Barra de Rolagem Minimalista
    scrollbar = tk.Scrollbar(frame_central, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Área de Exibição da Árvore
    # Usamos um widget 'Text' para permitir cores e formatação melhor que um Label
    label_resultado = tk.Text(
        janela, 
        height=10, 
        bg=COR_CARD, 
        fg=COR_ACENTO,
        font=("Consolas", 11), # Fonte monoespaçada para a árvore não quebrar
        padx=10,
        pady=10,
        borderwidth=0
    )
    label_resultado.pack(padx=20, pady=10, fill=tk.X)
    label_resultado.insert(tk.END, "A árvore de pré-requisitos aparecerá aqui...")
    label_resultado.config(state=tk.DISABLED) # Bloqueia digitação do usuário

    def atualizar_visualizacao():
        selecao = listbox.curselection()
        if not selecao: return
        
        materia = listbox.get(selecao[0])
        
        # Gera a árvore em texto (usando a lógica que criamos)
        arvore_texto = ""
        def gerar_texto_arvore(m, g, nivel=0):
            nonlocal arvore_texto
            prefixo = "    " * nivel + "└── " if nivel > 0 else ""
            arvore_texto += f"{prefixo}{m}\n"
            for disc, suc in g.items():
                if m in suc:
                    gerar_texto_arvore(disc, g, nivel + 1)

        gerar_texto_arvore(materia, grafo)
        
        # Atualiza o widget de texto
        label_resultado.config(state=tk.NORMAL)
        label_resultado.delete("1.0", tk.END)
        label_resultado.insert(tk.END, arvore_texto)
        label_resultado.config(state=tk.DISABLED)

    # Botão Moderno
    btn = tk.Button(
        janela, 
        text="GERAR ÁRVORE", 
        command=atualizar_visualizacao,
        bg=COR_ACENTO, 
        fg=COR_FUNDO,
        font=("Segoe UI", 10, "bold"),
        padx=20,
        pady=10,
        borderwidth=0,
        cursor="hand2"
    )
    btn.pack(pady=20)

    janela.mainloop()



# Para rodar:
# abrir_interface(disciplinas, grafo_pre_requisitos)