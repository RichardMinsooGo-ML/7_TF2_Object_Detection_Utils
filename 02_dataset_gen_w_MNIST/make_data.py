#================================================================
#
#   File name   : make_data.py
#   Author      : PyLessons
#   Created date: 2020-04-20
#   Website     : https://pylessons.com/
#   GitHub      : https://github.com/pythonlessons/TensorFlow-2.x-YOLOv3
#   Description : create mnist example dataset to train custom yolov3
#
#================================================================
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import cv2
import numpy as np
import shutil
import random
from zipfile import ZipFile 

SIZE = 416

images_num_train = 1000
images_num_val = 250
model_dir = "../01_1K_MNIST/"

# images_num_train = 13700
# images_num_val = 3425
# model_dir = "../11_14K_MNIST/"

# images_num_train = 117266
# images_num_val = 4952
# model_dir = "../21_117K_MNIST/"

image_sizes = [3, 6, 3] # small, medium, big

# this helps to run script both from terminal and python IDLE
add_path = "mnist"
if os.getcwd().split(os.sep)[-1] != "mnist":
    add_path = "mnist"
    os.chdir(add_path)
else:
    add_path = ""  
    
def compute_iou(box1, box2):
    # xmin, ymin, xmax, ymax
    A1 = (box1[2] - box1[0])*(box1[3] - box1[1])
    A2 = (box2[2] - box2[0])*(box2[3] - box2[1])

    xmin = max(box1[0], box2[0])
    ymin = max(box1[1], box2[1])
    xmax = min(box1[2], box2[2])
    ymax = min(box1[3], box2[3])

    if ymin >= ymax or xmin >= xmax: return 0
    return  ((xmax-xmin) * (ymax - ymin)) / (A1 + A2)


def make_image(data, image_path, ratio=1):
    blank = data[0]
    boxes = data[1]
    label = data[2]
    
    # print(image_path)

    # ID = image_path.split("/")[-1][0]
    ID = image_path.split("/")[-1]
    # print(ID)
    
    ID = ID.split("_")
    # print(ID)
    ID = ID[0]
    # print(ID)    
    
    image = cv2.imread(image_path)
    image = cv2.resize(image, (int(28*ratio), int(28*ratio)))
    h, w, c = image.shape

    while True:
        xmin = np.random.randint(0, SIZE-w, 1)[0]
        ymin = np.random.randint(0, SIZE-h, 1)[0]
        xmax = xmin + w
        ymax = ymin + h
        box = [xmin, ymin, xmax, ymax]

        iou = [compute_iou(box, b) for b in boxes]
        if max(iou) < 0.02:
            boxes.append(box)
            label.append(ID)
            break

    for i in range(w):
        for j in range(h):
            x = xmin + i
            y = ymin + j
            blank[y][x] = image[j][i]

    # cv2.rectangle(blank, (xmin, ymin), (xmax, ymax), [0, 0, 255], 2)
    return blank

"""
for file in ["train", "val"]:
    if not os.path.exists(f"mnist/{file}"):
        with ZipFile(f"mnist/{file}.zip", 'r') as zip:
            # extracting all the files 
            print(f'Extracting all {file} files now...') 
            zip.extractall()
            shutil.move(file, "mnist")
            print('Done!')
"""

for file in ['train','test']:
    # images_path = os.getcwd()+f"/mnist_{file}"
    # labels_txt = os.getcwd()+f"/mnist_{file}.txt"
    
    images_path = os.getcwd()+f"/mnist_{file}"
    labels_txt = os.getcwd()+f"/mnist_{file}.txt"
    tmp_labels_txt = os.getcwd()+f"/tmp_mnist_{file}.txt"
    
    if file == 'train':
        images_num = images_num_train
        image_dir = model_dir+"mnist_train/"
    if file == 'test':
        images_num = images_num_val
        image_dir = model_dir+"mnist_val/"
        
    if os.path.exists(images_path): shutil.rmtree(images_path)
    os.mkdir(images_path)

    image_paths  = [os.path.join(os.path.realpath("."), os.getcwd()+f"/{file}/" + image_name)
                           for image_name in os.listdir(os.getcwd()+f"/{file}")]
    # with open("file_1.txt") as f1, open("file_2.txt") as f2:
    with open(labels_txt, "w") as wf, open(tmp_labels_txt, "w") as tmp_wf:
        image_num = 0
        while image_num < images_num:
            image_path = os.path.realpath(os.path.join(images_path, "%06d.jpg" %(image_num+1)))
            # image_path = os.path.realpath("%06d" %(image_num+1))
            #print(image_path)
            annotation = "%06d.jpg" %(image_num+1)
            tmp_annotation = "%06d" %(image_num+1)
            # annotation = ""
            blanks = np.ones(shape=[SIZE, SIZE, 3]) * 255
            bboxes = [[0,0,1,1]]
            labels = [0]
            
            data = [blanks, bboxes, labels]
            bboxes_num = 0
            
            # ratios small, medium, big objects
            ratios = [[0.5, 0.8], [1., 1.5, 2.], [3., 4.]]
            for i in range(len(ratios)):
                N = random.randint(0, image_sizes[i])
                if N !=0: bboxes_num += 1
                for _ in range(N):
                    ratio = random.choice(ratios[i])
                    idx = random.randint(0, len(image_paths)-1)
                    data[0] = make_image(data, image_paths[idx], ratio)

            if bboxes_num == 0: continue
            cv2.imwrite(image_path, data[0])
            
            # print(labels)
            
            for i in range(len(labels)):
                if i == 0: continue
                xmin = str(bboxes[i][0])
                ymin = str(bboxes[i][1])
                xmax = str(bboxes[i][2])
                ymax = str(bboxes[i][3])
                class_ind = str(labels[i])
                annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, str(class_ind)])
                tmp_annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, str(class_ind)])
                # print(class_ind)
            
            image_num += 1
            if image_num%100 == 0:
                print("=> %s" %annotation)
            wf.write(image_dir+annotation + "\n")
            tmp_wf.write(tmp_annotation + "\n")

if add_path != "": os.chdir("..")
