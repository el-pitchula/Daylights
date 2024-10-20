import tkinter as tk
from tkinter import ttk

class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nosferatus Portfolio Editor")

        # Configurar a janela principal
        self.root.geometry("800x600")  # Tamanho da janela

        # Configurar a grid de conteúdo
        self.create_grid()

        # Criar a barra lateral de configurações
        self.create_sidebar()

    def create_grid(self):
        # Frame que contém o grid
        self.grid_frame = ttk.Frame(self.root, padding=10, relief="solid")
        self.grid_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Configurar colunas e linhas do grid
        for i in range(4):  # 4 colunas
            self.grid_frame.columnconfigure(i, weight=1, minsize=150)
        for i in range(3):  # 3 linhas
            self.grid_frame.rowconfigure(i, weight=1, minsize=150)

        # Adicionar widgets aos quadrados do grid
        self.grid_widgets = {}
        for row in range(3):
            for col in range(4):
                widget_frame = ttk.Frame(self.grid_frame, relief="solid", borderwidth=1)
                widget_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

                # Botão para adicionar conteúdo
                add_button = ttk.Button(widget_frame, text="Adicionar", command=lambda r=row, c=col: self.add_content(r, c))
                add_button.pack(expand=True)

                # Salvando referências dos widgets
                self.grid_widgets[(row, col)] = widget_frame

    def create_sidebar(self):
        # Frame da barra lateral
        self.sidebar = ttk.Frame(self.root, padding=10, relief="solid")
        self.sidebar.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Botão para adicionar Texto
        text_button = ttk.Button(self.sidebar, text="Adicionar Texto", command=self.add_text)
        text_button.pack(fill='x', pady=5)

        # Botão para adicionar API
        api_button = ttk.Button(self.sidebar, text="Adicionar API (Spotify)", command=self.add_api)
        api_button.pack(fill='x', pady=5)

    def add_content(self, row, col):
        print(f"Conteúdo adicionado no quadrado ({row}, {col})")
        # Aqui, você poderia abrir uma nova janela para adicionar o conteúdo desejado

    def add_text(self):
        print("Adicionando texto ao quadrado selecionado")
        # Lógica para adicionar texto ao grid ou uma célula específica

    def add_api(self):
        print("Adicionando integração com API")
        # Lógica para conectar a uma API, como o Spotify

# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioApp(root)
    root.mainloop()
