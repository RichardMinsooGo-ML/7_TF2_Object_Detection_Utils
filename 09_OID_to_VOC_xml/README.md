# KR

    OID format 을 Pascal VOC format으로 변환하는 모듈이 Python 에 존재한다.
    
    모듈을 아래와 같이 설정한다.
    
    Training set의 경우 시간이 상당히 걸린다. 2시간 이상 소요 될수 있으므로 가능하면 밤에 작업을 걸어 놓는게 편하다.
    
    08_OID_download 에서 만들어진 csv 파일을 이용하여 conversion 시킨다.

## Step 1

    pip install oidv6-to-voc


## Step 2

    oidv6-to-voc [filelist for convert] -d class-descriptions-boxable.csv --imgd [image path] --outd [xmlpath]
    oidv6-to-voc train/csv_for_train.csv -d class-descriptions-boxable.csv --imgd train/images_train --outd train/xml_train



### Template level 3

Add comment for level 3


### Template level 3

Add comment for level 3


