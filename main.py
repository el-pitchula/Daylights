import tkinter as tk
from tkinter import ttk
from tkinter import font

# Função para criar botões com ícones e cores
def create_icon_button(parent, text, color, symbol, style_name):
    # Criar o botão com o estilo personalizado
    btn = ttk.Button(parent, text=f"{symbol} {text}", style=style_name)
    btn.pack(padx=10, pady=5)
    return btn

# Configurações iniciais da janela principal
root = tk.Tk()
root.title("Editor de Portfólio")
root.geometry("900x600")
root.configure(bg="#2b2b2b")

# Definir uma fonte customizada para o projeto
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Estilo personalizado
style = ttk.Style()
style.configure("TFrame", background="#2b2b2b")
style.configure("TLabel", background="#2b2b2b", foreground="white", font=custom_font)
style.configure("TButton", padding=6, font=("Helvetica", 10))
style.configure("TLabelframe", background="#2b2b2b", foreground="white", font=custom_font)

# Estilo para botões com cores personalizadas
style.configure("Green.TButton", foreground="white", background="#4CAF50")
style.map("Green.TButton", foreground=[('active', 'white')], background=[('active', '#45a049')])

style.configure("Yellow.TButton", foreground="black", background="#FFC107")
style.map("Yellow.TButton", foreground=[('active', 'black')], background=[('active', '#e0a800')])

style.configure("Blue.TButton", foreground="white", background="#2196F3")
style.map("Blue.TButton", foreground=[('active', 'white')], background=[('active', '#1976D2')])

style.configure("Orange.TButton", foreground="white", background="#FF5722")
style.map("Orange.TButton", foreground=[('active', 'white')], background=[('active', '#E64A19')])

# Frame principal para conter o layout
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Frames laterais para Layers e Arquivos
left_frame = ttk.Frame(main_frame, width=200)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

# Área principal de Grid para layers
grid_frame = ttk.Frame(main_frame)
grid_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Ferramentas do lado direito
right_frame = ttk.Frame(main_frame, width=70)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

# -------- Seção de Layers --------
layers_label = ttk.Label(left_frame, text="Layers", font=("Helvetica", 14, "bold"))
layers_label.pack(anchor="nw", padx=5, pady=5)

# Lista de layers com cor de fundo e texto branco
layers_list = tk.Listbox(left_frame, bg="#474747", fg="white", bd=0, highlightthickness=0)
layers_list.insert(1, "Layer 1")
layers_list.insert(2, "Layer 2")
layers_list.pack(padx=5, pady=5, fill="y", expand=True)

# -------- Seção de Arquivos --------
files_label = ttk.Label(left_frame, text="Arquivos", font=("Helvetica", 14, "bold"))
files_label.pack(anchor="nw", padx=5, pady=10)

# Lista de arquivos com cor de fundo e texto branco
files_list = tk.Listbox(left_frame, bg="#474747", fg="white", bd=0, highlightthickness=0)
files_list.insert(1, "img1.png")
files_list.insert(2, "gif1.gif")
files_list.pack(padx=5, pady=5, fill="y", expand=True)

# -------- Grid Central --------
for i in range(4):  # Cria 4 linhas
    for j in range(4):  # Cria 4 colunas
        square = ttk.Frame(grid_frame, width=100, height=100, relief="solid", borderwidth=1)
        square.grid(row=i, column=j, padx=5, pady=5)

# -------- Ferramentas Laterais com Ícones e Cores --------
tools_label = ttk.Label(right_frame, text="Ferramentas", font=("Helvetica", 14, "bold"))
tools_label.pack(pady=10)

# Criar botões com ícones e estilos personalizados
save_button = create_icon_button(right_frame, "", "#4CAF50", "💾", "Green.TButton")  # Ícone de disquete (salvar)
comments_button = create_icon_button(right_frame, "", "#FFC107", "💬", "Yellow.TButton")  # Ícone de balão de fala (comentário)
zoom_in_button = create_icon_button(right_frame, "+", "#2196F3", "🔍+", "Blue.TButton")  # Ícone de lupa com mais
zoom_out_button = create_icon_button(right_frame, "-", "#FF5722", "🔍-", "Orange.TButton")  # Ícone de lupa com menos

# Inicia o loop da interface
root.mainloop()
