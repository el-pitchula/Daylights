# scripts/open_tkinter_interface.py
import tkinter as tk
from tkinter import ttk
import json

def save_data(user_input):
    data = {"user_input": user_input}
    with open("data/data.json", "w") as file:
        json.dump(data, file)

def create_interface():
    root = tk.Tk()
    root.title("Interactive Computer")

    label = ttk.Label(root, text="Digite algo:")
    label.pack(padx=20, pady=20)

    entry = ttk.Entry(root)
    entry.pack(padx=20, pady=20)

    def on_submit():
        user_input = entry.get()
        save_data(user_input)  # Salva os dados no arquivo data.json
        root.quit()

    button = ttk.Button(root, text="Enviar", command=on_submit)
    button.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_interface()
