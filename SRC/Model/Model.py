import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2

imgOrigin = None
img = None
imgPath = None

def load_img():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath)
        if img is not None:
            print('Original')
            cv2.imshow('Original', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('Erro ao carregar a imagem')
    

def gray_color():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            print('Gray')
            cv2.imshow('Gray', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('Erro ao carregar a imagem')
   

def binary_color():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
        if img is not None:

            threshold = 128

            ret, binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    
            # Exibe a imagem binarizada
            print('Binary')
            cv2.imshow('Binário', binary)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def gaussian_filter():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath)
        if img is not None:
            kernelSize = (3, 3)
            standardDeviation = 0
            gaussian = cv2.GaussianBlur(img, kernelSize, standardDeviation)


            print('Gaussiana')
            cv2.imshow('Gaussiana', gaussian)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def median_filter():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath)
        if img is not None:
            median = cv2.medianBlur(img, 3)

            print('Mediana')
            cv2.imshow('Mediana', median)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def canny_edge():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath)
        if img is not None:
            img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
            edges = cv2.Canny(img, 100, 200)

            # Define uma máscara preenchida com zeros
            mask = np.zeros_like(img)

            # Preenche a máscara com valores brancos nos locais das bordas detectadas
            mask[edges != 0] = 255

            # Exibe a detecção de bordas Canny
            print('Canny')
            cv2.imshow('Canny', edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def laplace_edge():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath)
        if img is not None:
            laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize=3)

            print('Laplacian')
            cv2.imshow('Laplacian', laplacian)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


def sobel_edge():
    # Abre a caixa de diálogo para seleção do arquivo
    global imgOrigin, img, imgPath
    imgPath = filedialog.askopenfilename()
    if imgPath:
        img = cv2.imread(imgPath)
        if img is not None:
            img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

    
            sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
            sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

            # Calcula a magnitude das derivadas
            sobelMag = np.sqrt(sobelX**2 + sobelY**2)

            # Converte os valores para o intervalo de 0 a 255
            sobelMag = np.uint8(sobelMag)

            # Exibe as imagens de saída
            print('Sobel')
            cv2.imshow('Sobel X', sobelX)
            cv2.imshow('Sobel Y', sobelY)
            cv2.imshow('Magnitude do Sobel', sobelMag)
            cv2.waitKey(0)
            cv2.destroyAllWindows()