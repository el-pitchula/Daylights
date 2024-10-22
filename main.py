import tkinter as tk
from tkinter import ttk

# Configurações iniciais da janela principal
root = tk.Tk()
root.title("letters")
root.geometry("800x600")

# Frame principal para conter o layout
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Frames laterais para Layers e Arquivos
left_frame = ttk.Frame(main_frame, width=200)
left_frame.pack(side="left", fill="y")

# Área principal de Grid para layers
grid_frame = ttk.Frame(main_frame)
grid_frame.pack(side="left", fill="both", expand=True)

# Ferramentas do lado direito
right_frame = ttk.Frame(main_frame, width=50)
right_frame.pack(side="right", fill="y")

# -------- Seção de Layers --------
layers_label = ttk.Label(left_frame, text="Layers", font=("Arial", 12))
layers_label.pack(anchor="nw", padx=10, pady=10)

# Lista de layers
layers_list = tk.Listbox(left_frame)
layers_list.insert(1, "Layer 1")
layers_list.insert(2, "Layer 2")
layers_list.pack(padx=10, pady=5, fill="y", expand=True)

# -------- Seção de Arquivos --------
files_label = ttk.Label(left_frame, text="Arquivos", font=("Arial", 12))
files_label.pack(anchor="nw", padx=10, pady=10)

# Lista de arquivos
files_list = tk.Listbox(left_frame)
files_list.insert(1, "img1.png")
files_list.insert(2, "gif1.gif")
files_list.pack(padx=10, pady=5, fill="y", expand=True)

# -------- Grid Central --------
for i in range(4):  # Cria 4 linhas
    for j in range(4):  # Cria 4 colunas
        square = ttk.Frame(grid_frame, width=100, height=100, relief="solid", borderwidth=1)
        square.grid(row=i, column=j, padx=5, pady=5)

# -------- Ferramentas Laterais --------
save_button = ttk.Button(right_frame, text="Salvar")
save_button.pack(padx=5, pady=20)

comments_button = ttk.Button(right_frame, text="Comentários")
comments_button.pack(padx=5, pady=20)

zoom_button = ttk.Button(right_frame, text="Zoom")
zoom_button.pack(padx=5, pady=20)

# Inicia o loop da interface
root.mainloop()
