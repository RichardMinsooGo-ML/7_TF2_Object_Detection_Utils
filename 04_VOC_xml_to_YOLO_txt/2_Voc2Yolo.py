import xml.etree.ElementTree as ET
from os import getcwd

# sets=[('2012', 'train'), ('2012', 'val')]

class_path = "./voc2012.names"

classes = [c.strip() for c in open(class_path).readlines()]

print(classes)

# import sys
# sys.exit()


def convert_annotation(image_id, list_file):
    in_file = open(xml_path+'/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

#-----------------------------------        
image_ids = open('./train.txt').read().strip().split()
list_file = open('MNIST_train_Yolo.txt', 'w')

xml_path = "train_xml"

for image_id in image_ids:
    list_file.write('./images_train/%s.jpg'%(image_id))
    convert_annotation(image_id, list_file)
    list_file.write('\n')
list_file.close()

#-----------------------------------        
image_ids = open('./val.txt').read().strip().split()
list_file = open('MNIST_val_Yolo.txt', 'w')

xml_path = "val_xml"

for image_id in image_ids:
    list_file.write('./images_val/%s.jpg'%(image_id))
    convert_annotation(image_id, list_file)
    list_file.write('\n')
list_file.close()






