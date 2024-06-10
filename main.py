import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist


PATH_FOLHA = "folhas.jpg"
PATH_FOLHA_RETICULADO = "folhas_Reticulados.jpg"

def open_image(im:str)->object:
    return Image.open(im).convert('L')

def dft(im:object)->object:
    ...

def dft_inverse(im:object)->object:
    ...

def main(path:str, result_file_name:str)->None:
    ...

if __name__ == "__main__":
    # main(PATH_FOLHA, "folha")
    ...