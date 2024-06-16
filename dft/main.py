import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist


PATH_FOLHA = "images/folhas.jpg"
PATH_FOLHA_RETICULADA = "images/folhas_Reticulada.jpg"

if __name__ == "__main__":
    # Abra a imagem
    folha_image = imread(PATH_FOLHA_RETICULADA, as_gray=True)

    folha_image_fourier = np.fft.fftshift(np.fft.fft2(folha_image))

    plt.imshow(np.log(abs(folha_image_fourier)), cmap='gray')
    plt.savefig("results/folha_fourier.png")

    # Aplicando mascara
    f_size = 15

    folha_image_fourier[:581, 953:977] = 1
    folha_image_fourier[-581:,953:977] = 1 

    folha_image_fourier[580:610, :923] = 1
    folha_image_fourier[580:610,-923:] = 1 

    plt.imshow(np.log(abs(folha_image_fourier)), cmap='gray')
    plt.savefig("results/folha_mask_fourier.png")

    plt.show()

    folha_image_inverse_fourier = abs(np.fft.ifft2(folha_image_fourier))

    plt.imshow(folha_image_inverse_fourier, cmap='gray')
    plt.savefig("results/folha_inverse_fourier.png")
    



