# KR

해당 폴더에서는 OID dataset을 부터 원하는 class 데이터셋을 다운로드 받는 법에 대해서 다룬다.

예제 파일은 30 개의 class로 이루어져 있다.

## Step 1 : Download class and annotation files

* Download lists

      class-descriptions-boxable.csv
      oidv6-train-annotations-bbox.csv
      test-annotations-bbox.csv
      validation-annotations-bbox.csv

Download class file and annotation files from OID official site or from my Google Drive.

* OID V6 official site :
https://storage.googleapis.com/openimages/web/index.html

* My Google Drive :
https://drive.google.com/drive/folders/1H6daKQjZWsgalg3eXeKObVb__OlYbYFD?usp=sharing

## Step 2 : Select classes for customizing

수작업으로 class_for_customizing.csv 와 OID_V6.names 를 만들어 준다.

* (원본 파일) class-descriptions-boxable.csv 로 부터 customizing 하고자 하는 30개 의 class를 선택하여서 class_for_customizing.csv와 같은 파일을 만든다.

* 향후 프로그램에 사용하기 위해서 class 파일을 OID_V6.names와 같이 만든다.

## Step 3 : Build the list for download


### Template level 3

Add comment for level 3



# EN

In this folder have an example of Download cusomized datasets.

There are 30 classes sample. Please follow step by step.


