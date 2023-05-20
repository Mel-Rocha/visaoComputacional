import tkinter as tk
from tkinter import filedialog
import cv2

imgOrigin = None
img = None
file_path = None

def case_original():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        if img is not None:
            cv2.imshow('Original', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('Erro ao carregar a imagem')
    else:
        print('Nenhum arquivo selecionado')

def case_gray():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            cv2.imshow('Cinza', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('Erro ao carregar a imagem')
    else:
        print('Nenhum arquivo selecionado')

