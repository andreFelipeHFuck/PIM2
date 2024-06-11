import cv2 

PATH = "video.mp4"

def frameCapture(path):
    video = cv2.VideoCapture(path)

    count = 0
    sucess = 1

    while sucess:
        sucess, image = video.read()

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("frame/frame%d.jpg" % count, image_gray)
        count += 1


if __name__ == '__main__':
    frameCapture(PATH)