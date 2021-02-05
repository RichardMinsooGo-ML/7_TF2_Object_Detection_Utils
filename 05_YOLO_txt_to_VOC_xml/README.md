## KR

해당 폴더에는 text 형태를 Pascal VOC 형태로 변환시켜 주는 파이썬 파일이 있다.

### Step 1 : tempporary text 파일 생성 

VOC2012_train.txt --> tmp_VOC2012_train.txt

VOC2012_val.txt   --> tmp_VOC2012_val.txt

와 같이 이미지 경로와, 확장자를 제거하여 준다. 

이부분을 pandas로 구현하면 버그가 있다. 어렵지 않은 작업이니 수작으로 하는 편이 빠르다.

원본파일은 다음과 같다.

    ../03_mini_VOC2012/train_images/2007_000033.jpg 9,107,499,263,0 421,200,482,226,0 325,188,411,223,0
    ../03_mini_VOC2012/train_images/2007_000243.jpg 181,127,274,193,0
    ../03_mini_VOC2012/train_images/2007_000464.jpg 71,252,216,314,9 58,202,241,295,9
    ../03_mini_VOC2012/train_images/2007_000645.jpg 135,46,500,374,2 124,146,365,375,2
    ../03_mini_VOC2012/train_images/2007_000925.jpg 29,101,216,343,16 309,105,460,333,16
    ../03_mini_VOC2012/train_images/2007_001299.jpg 39,26,229,412,9 211,240,319,408,9 318,221,408,435,9
    ../03_mini_VOC2012/train_images/2007_001458.jpg 106,121,392,299,17

아래와 같이 만들어 준다.

    2007_000033 9,107,499,263,0 421,200,482,226,0 325,188,411,223,0
    2007_000243 181,127,274,193,0
    2007_000464 71,252,216,314,9 58,202,241,295,9
    2007_000645 135,46,500,374,2 124,146,365,375,2
    2007_000925 29,101,216,343,16 309,105,460,333,16
    2007_001299 39,26,229,412,9 211,240,319,408,9 318,221,408,435,9
    2007_001458 106,121,392,299,17

### Step 2 : 파이썬 파일을 싱행시키면 된다.

    1_generate_txt_files.py
    2_yolo_to_voc_xml.py


## EN

In this folder, there is python files that can generate Pascal VOC xml from text format.

### Step 1 : Build tempporary text manually

Remove, image directory and extendor like a sample :

VOC2012_train.txt --> tmp_VOC2012_train.txt

VOC2012_val.txt   --> tmp_VOC2012_val.txt

When I realize it by pandas, I fouund some bugs. So, it is more efficient to remove by manually.

Original exte file like this.

    ../03_mini_VOC2012/train_images/2007_000033.jpg 9,107,499,263,0 421,200,482,226,0 325,188,411,223,0
    ../03_mini_VOC2012/train_images/2007_000243.jpg 181,127,274,193,0
    ../03_mini_VOC2012/train_images/2007_000464.jpg 71,252,216,314,9 58,202,241,295,9
    ../03_mini_VOC2012/train_images/2007_000645.jpg 135,46,500,374,2 124,146,365,375,2
    ../03_mini_VOC2012/train_images/2007_000925.jpg 29,101,216,343,16 309,105,460,333,16
    ../03_mini_VOC2012/train_images/2007_001299.jpg 39,26,229,412,9 211,240,319,408,9 318,221,408,435,9
    ../03_mini_VOC2012/train_images/2007_001458.jpg 106,121,392,299,17

User shall remove like below:

    2007_000033 9,107,499,263,0 421,200,482,226,0 325,188,411,223,0
    2007_000243 181,127,274,193,0
    2007_000464 71,252,216,314,9 58,202,241,295,9
    2007_000645 135,46,500,374,2 124,146,365,375,2
    2007_000925 29,101,216,343,16 309,105,460,333,16
    2007_001299 39,26,229,412,9 211,240,319,408,9 318,221,408,435,9
    2007_001458 106,121,392,299,17

### Step 2 : Then execute python files.

    1_generate_txt_files.py
    2_yolo_to_voc_xml.py

