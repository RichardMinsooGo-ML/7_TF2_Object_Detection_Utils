# KR

해당 폴더에서는 OID dataset을 부터 원하는 class 데이터셋을 다운로드 받는 법에 대해서 다룬다.

예제 파일은 30 개의 class로 이루어져 있다.

## Step 1 : Download class and annotation files

* 준비물

      class-descriptions-boxable.csv
      oidv6-train-annotations-bbox.csv
      test-annotations-bbox.csv
      validation-annotations-bbox.csv

위 네개의 파일을 "OID official site" 나 필자가 운영하는 구글 드라이브에서 다운로드 받는다.
Download class file and annotation files from OID official site or from my Google Drive.


* OID V6 official site :
https://storage.googleapis.com/openimages/web/index.html

* My Google Drive :
https://drive.google.com/drive/folders/1H6daKQjZWsgalg3eXeKObVb__OlYbYFD?usp=sharing

## Step 2 : Select classes for customizing

수작업으로 class_for_customizing.csv 와 OID_V6.names 를 만들어 준다.

* (원본 파일) class-descriptions-boxable.csv 로 부터 customizing 하고자 하는 30개 의 class를 선택하여서 class_for_customizing.csv와 같은 파일을 만든다.

* 향후 프로그램에 사용하기 위해서 class 파일을 OID_V6.names와 같이 만든다.

## Step 3 : Build the image list and annotation list

위의 네개의 파일은 모든 OID dataset 을 포함하고 있다.

따라서 파이선 파일을 사용하여 원하는 데이터만 추출한다. 

      python Generation_custom_img_list_n_anno_train.py
      python Generation_custom_img_list_n_anno_test.py
      python Generation_custom_img_list_n_anno_val.py

Customizing 할 경우에는 clssases list 를 편집하여 준다. class list 는 step 2 에서 만든 class_for_customizing.csv에서 가져 온다.

      new_data = data[data['LabelName'].isin(["/m/0120dh", "/m/012n7d", "/m/014j1m", "/m/01_5g", "/m/015p6", "/m/015qff", "/m/0174n1", 
                                              "/m/01940j", "/m/0199g", "/m/019w40", "/m/01bjv", "/m/01c648", "/m/01d380", "/m/01dws", 
                                              "/m/01fh4r", "/m/01h3n", "/m/01h8tj", "/m/01jfm_", "/m/01lcw4", "/m/01mzpv", "/m/01n4qj", 
                                              "/m/01x3jk", "/m/01x3z", "/m/01xs3r", "/m/01x_v", "/m/020jm", "/m/020kz", "/m/025fsf", 
                                              "/m/029b3", "/m/02hj4"]) ]

Sub-folder 에 결과를 저장하였다. 

### Step 4 : Download images

해당 폴더에는 다운로드 프로그램이 있다. 이 프로그램은 OID official site 에서도 제공한다.

      python downloader.py [custom image list] --download_folder=[folder name] --num_processes=[classes number]
      python downloader.py val/img_list_custom_val.txt --download_folder=images_val --num_processes=30
      python downloader.py test/img_list_custom_test.txt --download_folder=images_test --num_processes=30
      python downloader.py train/img_list_custom_train.txt --download_folder=images_train --num_processes=30

위 작업을 수행하는데는 몇시간이 걸릴수 있다.

다운로드 결과는 필자의 구글드라이브에 저장하였다. 

https://drive.google.com/drive/folders/1gKivkbJIWWhNxbSLqpVNOb1Izd8Yz9Yi?usp=sharing


# EN

In this folder have an example of Download cusomized datasets.

There are 30 classes sample. Please follow step by step.


해당 폴더에서는 OID dataset을 부터 원하는 class 데이터셋을 다운로드 받는 법에 대해서 다룬다.

예제 파일은 30 개의 class로 이루어져 있다.

## Step 1 : Download class and annotation files

* 준비물

      class-descriptions-boxable.csv
      oidv6-train-annotations-bbox.csv
      test-annotations-bbox.csv
      validation-annotations-bbox.csv

위 네개의 파일을 "OID official site" 나 필자가 운영하는 구글 드라이브에서 다운로드 받는다.
Download class file and annotation files from OID official site or from my Google Drive.


* OID V6 official site :
https://storage.googleapis.com/openimages/web/index.html

* My Google Drive :
https://drive.google.com/drive/folders/1H6daKQjZWsgalg3eXeKObVb__OlYbYFD?usp=sharing

## Step 2 : Select classes for customizing

수작업으로 class_for_customizing.csv 와 OID_V6.names 를 만들어 준다.

* (원본 파일) class-descriptions-boxable.csv 로 부터 customizing 하고자 하는 30개 의 class를 선택하여서 class_for_customizing.csv와 같은 파일을 만든다.

* 향후 프로그램에 사용하기 위해서 class 파일을 OID_V6.names와 같이 만든다.

## Step 3 : Build the image list and annotation list

위의 네개의 파일은 모든 OID dataset 을 포함하고 있다.

따라서 파이선 파일을 사용하여 원하는 데이터만 추출한다. 

      python Generation_custom_img_list_n_anno_train.py
      python Generation_custom_img_list_n_anno_test.py
      python Generation_custom_img_list_n_anno_val.py

Customizing 할 경우에는 clssases list 를 편집하여 준다. class list 는 step 2 에서 만든 class_for_customizing.csv에서 가져 온다.

      new_data = data[data['LabelName'].isin(["/m/0120dh", "/m/012n7d", "/m/014j1m", "/m/01_5g", "/m/015p6", "/m/015qff", "/m/0174n1", 
                                              "/m/01940j", "/m/0199g", "/m/019w40", "/m/01bjv", "/m/01c648", "/m/01d380", "/m/01dws", 
                                              "/m/01fh4r", "/m/01h3n", "/m/01h8tj", "/m/01jfm_", "/m/01lcw4", "/m/01mzpv", "/m/01n4qj", 
                                              "/m/01x3jk", "/m/01x3z", "/m/01xs3r", "/m/01x_v", "/m/020jm", "/m/020kz", "/m/025fsf", 
                                              "/m/029b3", "/m/02hj4"]) ]

Sub-folder 에 결과를 저장하였다. 

### Step 4 : Download images

해당 폴더에는 다운로드 프로그램이 있다. 이 프로그램은 OID official site 에서도 제공한다.

      python downloader.py [custom image list] --download_folder=[folder name] --num_processes=[classes number]
      python downloader.py val/img_list_custom_val.txt --download_folder=images_val --num_processes=30
      python downloader.py test/img_list_custom_test.txt --download_folder=images_test --num_processes=30
      python downloader.py train/img_list_custom_train.txt --download_folder=images_train --num_processes=30

위 작업을 수행하는데는 몇시간이 걸릴수 있다.

다운로드 결과는 필자의 구글드라이브에 저장하였다. 

https://drive.google.com/drive/folders/1gKivkbJIWWhNxbSLqpVNOb1Izd8Yz9Yi?usp=sharing


