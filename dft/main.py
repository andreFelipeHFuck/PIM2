import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist


PATH_FOLHA = "images/folhas.jpg"
PATH_FOLHA_RETICULADA = "images/folhas_Reticulada.jpg"

"""
fig, ax = plt.subplots(1,3,figsize=(15,15))

    ax[0].imshow(np.log(abs(folha_image_fourier)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize = f_size)

    ax[1].imshow(folha_image, cmap = 'gray')
    ax[1].set_title('Greyscale Image', fontsize = f_size)

    ax[2].imshow(abs(np.fft.ifft2(folha_image_fourier)), cmap='gray')
    ax[2].set_title('Transformed Greyscale Image', fontsize = f_size)

"""

if __name__ == "__main__":
    # Abra a imagem
    folha_image = imread(PATH_FOLHA_RETICULADA, as_gray=True)

    folha_image_fourier = np.fft.fftshift(np.fft.fft2(folha_image))

    plt.imshow(np.log(abs(folha_image_fourier)), cmap='gray')
    plt.savefig("results/folha_fourier.png")

    # Tamanho da imagem
    height, width = folha_image_fourier.shape

    print(height)
    print(width)


    # Aplicando mascara
    f_size = 15

    folha_image_fourier[:575, 959:961] = 1
    folha_image_fourier[-575:,959:961] = 1 

    plt.imshow(np.log(abs(folha_image_fourier)), cmap='gray')
    plt.savefig("results/folha_mask_fourier.png")

    plt.show()

    folha_image_inverse_fourier = abs(np.fft.ifft2(folha_image_fourier))

    plt.imshow(folha_image_inverse_fourier, cmap='gray')
    plt.savefig("results/folha_inverse_fourier.png")
    



