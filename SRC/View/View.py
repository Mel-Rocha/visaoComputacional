import tkinter as tk
from ..Model.Model import case_original, case_gray


def start_gui():
    # Cria a janela da interface gráfica
    root = tk.Tk()

    # Cria o botão para exibir a imagem original
    button_original = tk.Button(root, text="Original", command=case_original)
    button_original.pack()

    # Cria o botão para exibir a imagem em escala de cinza
    button_gray = tk.Button(root, text="Cinza", command=case_gray)
    button_gray.pack()

    # Inicia o loop da interface gráfica
    root.mainloop()
