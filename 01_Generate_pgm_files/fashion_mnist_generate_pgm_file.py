# example of loading the fashion mnist dataset
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load the CIFAR-10 dataset
fashion_mnist  = tf.keras.datasets.fashion_mnist 

# Get test and training data where x are the images and y are the labels
# load dataset
(trainX, trainy), (testX, testy) = fashion_mnist .load_data()

# 32 pixel is used at Mobilenetv2 ,resnet152, ... etc.
# if you want to use other network, please find the input size. 
img_size = 28

# summarize loaded dataset
print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
print('Test: X=%s, y=%s' % (testX.shape, testy.shape))

LABELS_LIST = [
    'T-shirt/top', 
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle_boot'
]


for idx in range (60000):
    your_image = trainX[idx]
    
    # plt.imshow(your_image, cmap=plt.get_cmap('gray'))
    # plt.show()
    
    # your_image = np.abs(your_image - 255.)
    # import time
    # time.sleep(5)
    
    # plt.imshow(your_image, cmap=plt.get_cmap('gray'))
    # plt.show()
    
    
    your_image = cv2.resize(trainX[idx], (img_size, img_size), interpolation=cv2.INTER_CUBIC)
    fig = plt.figure(frameon=False)
    fig.set_size_inches(2,2)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(your_image, aspect='auto')
    
    # pyplot.imshow(trainX[i], cmap=pyplot.get_cmap('gray'))
    
    # Convert to grey
    # gray = cv2.cvtColor(your_image, cv2.COLOR_BGR2GRAY)
    # gray = your_image
    gray = np.abs(your_image - 255.)

    cv2.imwrite('./train/'+str(10+int(trainy[idx]))+'_'+str(idx).zfill(5)+'.pgm',gray)
    
    plt.close('all')
    if (idx+1) % 100 ==0:
        print(idx+1,"train images were converted and saved!")

for idx in range (10000):
    your_image = testX[idx]
    # your_image = np.abs(your_image - 255.)
    your_image = cv2.resize(testX[idx], (img_size, img_size), interpolation=cv2.INTER_CUBIC)
    fig = plt.figure(frameon=False)
    fig.set_size_inches(2,2)

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(your_image, aspect='auto')
    
    # Convert to grey
    # gray = cv2.cvtColor(your_image, cv2.COLOR_BGR2GRAY)
    # gray = your_image
    gray = np.abs(your_image - 255.)

    cv2.imwrite('./test/'+str(10+int(testy[idx]))+'_'+str(idx).zfill(5)+'.pgm',gray)

    plt.close('all')
    if (idx+1) % 100 ==0:
        print(idx+1,"test images were converted and saved!")
