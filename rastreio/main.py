import cv2 
import csv
import os
import matplotlib.pyplot as plt

PATH_FRAMES_DIR = "frames"
PATH_RESULTS_DIR = "results"
PATH_TEMPLATE = "template.png"
PATH_FIRST_FRAME = f'{PATH_FRAMES_DIR}/frame_0000.png'

first_frame = cv2.imread(PATH_FIRST_FRAME, 0)
video_h, video_w = first_frame.shape[:2]

template = cv2.imread(PATH_TEMPLATE, 0)
template_w, template_h = template.shape[::-1]

methods = [
    'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
    'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 
    'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED' 
]

def save_results(resulst, meth:str):
    with open(f'{PATH_RESULTS_DIR}/{meth[4:]}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Quadro', 'Min_Val', 'Max_Val'])
        writer.writerows(resulst)

def analysi_method(meth:str)->None:
    results = []
    marked_frames = []
    
    for frame_filename in sorted(os.listdir(PATH_FRAMES_DIR)):
        frame = cv2.imread(f'{PATH_FRAMES_DIR}/{frame_filename}', 0)
        method = eval(meth)

        res = cv2.matchTemplate(frame, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)

        results.append([frame_filename, min_val, max_val])

    save_results(results, meth)

def analysis_methods()->None:
    for meth in methods:
        print(f'Método as ser análisado: {meth}')
        analysi_method(meth)
        print("Fim da analise")

def graphic_method(meth:str)->None:
    quadros = []
    min_vals = []
    max_vals = []

    with open(os.path.join('results', f'TM_CCOEFF_NORMED.csv'), newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            quadro, min_val, max_val = row
            quadros.append(quadro[6:9])
            min_vals.append(float(min_val))
            max_vals.append(float(max_val))

    plt.figure(figsize=(10, 6))
    plt.plot(quadros, min_vals, label='Min_Val')
    plt.plot(quadros, max_vals, label='Max_Val')
    plt.legend(loc="upper left")
    plt.title(f'Resultados do Método {meth[4:]}')
    plt.xlabel('Quadros')
    plt.ylabel('Valor')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.grid(False)
    plt.savefig(f'results/{meth[4:]}.png')

def graphics_methods()->None:
    for meth in methods:
        graphic_method(meth)

def tracking(meth:str)->None:
    marked_frames = []
    
    for frame_filename in sorted(os.listdir(PATH_FRAMES_DIR)):
        frame = cv2.imread(f'{PATH_FRAMES_DIR}/{frame_filename}', 0)
        method = eval(meth)

        res = cv2.matchTemplate(frame, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)

        marked_frame = frame #cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(marked_frame, top_left, bottom_right, (0, 0, 255), 2)
        marked_frames.append(marked_frame)

        cv2.imwrite(f'teste/{frame_filename}', marked_frame)


    # out = cv2.VideoWriter(f'results/{meth[4:]}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (video_w, video_h))
    # for marked_frame in marked_frames:
    #     out.write(marked_frame)
    # out.release()

def main()->None:
   tracking(methods[2])

if __name__ == '__main__':
    main()