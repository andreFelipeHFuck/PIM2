import cv2
import os

video_path = 'video.mp4'
output_dir = 'frames'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.png')

    cv2.imwrite(frame_filename, gray_frame)

    frame_count += 1

cap.release()

print(f'Extração de frames em tons de cinza concluída. {frame_count} frames salvos em {output_dir}.')
