import cv2
import os

# Diretório contendo as imagens
image_folder = 'teste'
# Nome do arquivo de saída
video_name = 'output_video.mp4'

# Obter a lista de arquivos no diretório e ordenar
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
images.sort()

# Verificar se há imagens no diretório
if not images:
    raise ValueError("No images found in the directory")

# Ler a primeira imagem para obter as dimensões do vídeo
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path, cv2.IMREAD_GRAYSCALE)  # Ler em preto e branco
height, width = frame.shape

# Definir o codec e criar o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para MP4
video = cv2.VideoWriter(video_name, fourcc, 1, (width, height), isColor=False)  # isColor=False para preto e branco

# Adicionar cada imagem ao vídeo
for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Ler em preto e branco
    video.write(frame)

# Libera o objeto VideoWriter
video.release()
cv2.destroyAllWindows()

print(f"Vídeo salvo como {video_name}")
