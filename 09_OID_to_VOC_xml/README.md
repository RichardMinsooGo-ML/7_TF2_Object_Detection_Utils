# KR

OID format 을 Pascal VOC format으로 변환하는 모듈이 Python 에 존재한다.

모듈을 아래와 같이 설정한다.

Training set의 경우 시간이 상당히 걸린다. 2시간 이상 소요 될수 있으므로 가능하면 밤에 작업을 걸어 놓는게 편하다.

08_OID_download 에서 만들어진 csv 파일과 image 파일을 이용하여 conversion 시킨다.

전체적인 폴더구조는 필자의 구글드라이브에서 가지고 온다.

https://drive.google.com/drive/folders/1gKivkbJIWWhNxbSLqpVNOb1Izd8Yz9Yi?usp=sharing

## Step 1

    pip install oidv6-to-voc


## Step 2

    oidv6-to-voc [custom annotation file] -d class-descriptions-boxable.csv --imgd [image directory] --outd [output xml directory]
    oidv6-to-voc annotations_custom_val.csv -d class-descriptions-boxable.csv --imgd images_val --outd xml_val
    oidv6-to-voc annotations_custom_test.csv -d class-descriptions-boxable.csv --imgd images_test --outd xml_test
    oidv6-to-voc annotations_custom_train.csv -d class-descriptions-boxable.csv --imgd images_train --outd xml_train


# EN

There is python module that can convert from OID datasets to Pascal VOC format.

You can install this module like Step 1.

In the case of training set, it takes long time. It might take more than 2~3 hours. If possible try it at night. Computer never sleeps

To try this one, you need image files/folder and custom annotation files that is generated at "08_OID_download".

You can download it from my Google Drive.

https://drive.google.com/drive/folders/1gKivkbJIWWhNxbSLqpVNOb1Izd8Yz9Yi?usp=sharing

## Step 1

    pip install oidv6-to-voc


## Step 2

    oidv6-to-voc [custom annotation file] -d class-descriptions-boxable.csv --imgd [image directory] --outd [output xml directory]
    oidv6-to-voc annotations_custom_val.csv -d class-descriptions-boxable.csv --imgd images_val --outd xml_val
    oidv6-to-voc annotations_custom_test.csv -d class-descriptions-boxable.csv --imgd images_test --outd xml_test
    oidv6-to-voc annotations_custom_train.csv -d class-descriptions-boxable.csv --imgd images_train --outd xml_train

