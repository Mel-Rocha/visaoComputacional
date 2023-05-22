import tkinter as tk
from ..Model.Model import load_img, gray_color, binary_color, gaussian_filter, median_filter, canny_edge, laplace_edge, sobel_edge

def start_gui():
    # Cria a janela da interface gráfica
    root = tk.Tk()
    root.geometry("800x500")  # Define as dimensões 
    root.title('Processamento de Imagem')
    # Cria o rótulo
    label = tk.Label(root, text="Opções de Processamento")
    label.grid(row=0, column=0)
    label.pack()
    

    # Cria o botão para exibir a imagem original
    button_original = tk.Button(root, text="Original", command=load_img)
    button_original.pack()

    # Cria o botão para exibir a imagem em escala de cinza
    button_gray = tk.Button(root, text="Gray", command=gray_color)
    button_gray.pack()

    # Cria o botão para exibir a imagem em 
    button_binary = tk.Button(root, text="Binary", command=binary_color)
    button_binary.pack()

    # Cria o botão para exibir a imagem em 
    button_gaussian = tk.Button(root, text="Gaussian", command=gaussian_filter)
    button_gaussian.pack()

    # Cria o botão para exibir a imagem em 
    button_median = tk.Button(root, text="Median", command=median_filter)
    button_median.pack()

    # Cria o botão para exibir a imagem em 
    button_canny = tk.Button(root, text="Canny", command=canny_edge)
    button_canny.pack()

    # Cria o botão para exibir a imagem em 
    button_laplace = tk.Button(root, text="Laplace", command=laplace_edge)
    button_laplace.pack()

    # Cria o botão para exibir a imagem em 
    button_sobel = tk.Button(root, text="Sobel", command=sobel_edge)
    button_sobel.pack()


    # Inicia o loop da interface gráfica
    root.mainloop()
    

    
    root.destroy()
    
    # Define a ação a ser executada quando o usuário fecha a janela
    root.protocol("WM_DELETE_WINDOW")

      

      