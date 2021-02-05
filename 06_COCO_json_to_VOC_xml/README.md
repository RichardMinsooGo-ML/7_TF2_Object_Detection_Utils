## KR

해당 폴더에서는 COCO json 파일의 포맷을 Pascal VOC xml 포맷으로 바꾸는 파이썬 파일이 있다.

해당 폴더와 같이 변환하고자 하는 COCO json 파일을 준비g후에 아래와 같이 실행한다.

    python coco2voc.py --json_path [Json file path]  --output [xml file path]
    python coco2voc.py --json_path instances_val2017.json  --output xml_val

## EN

In this folder, there is a python file that can generate Pascal VOC xml files from COCO json.

Prepare COCO json file like this folder and execute python file like below.

    python coco2voc.py --json_path [Json file path]  --output [xml file path]
    python coco2voc.py --json_path instances_val2017.json  --output xml_val

