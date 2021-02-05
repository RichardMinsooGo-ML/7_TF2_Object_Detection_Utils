import csv

# importing pandas module 
import pandas as pd 

import os
if not os.path.exists('test'):
    os.makedirs('test')
    
data = pd.read_csv("test-annotations-bbox.csv") 

# Select the class name for customizing
new_data = data[data['LabelName'].isin(["/m/0120dh", "/m/012n7d", "/m/014j1m", "/m/01_5g", "/m/015p6", "/m/015qff", "/m/0174n1", 
                                        "/m/01940j", "/m/0199g", "/m/019w40", "/m/01bjv", "/m/01c648", "/m/01d380", "/m/01dws", 
                                        "/m/01fh4r", "/m/01h3n", "/m/01h8tj", "/m/01jfm_", "/m/01lcw4", "/m/01mzpv", "/m/01n4qj", 
                                        "/m/01x3jk", "/m/01x3z", "/m/01xs3r", "/m/01x_v", "/m/020jm", "/m/020kz", "/m/025fsf", 
                                        "/m/029b3", "/m/02hj4"]) ]

new_data.to_csv("./test/annotations_custom_test.csv", index=False)

# Generation of download image lists
new_csv = new_data.groupby((new_data["ImageID"] != new_data["ImageID"].shift()).cumsum().values).first()
new_csv['ImageID'] = 'test/' + new_csv['ImageID'].astype(str)

saved_csv = new_csv.drop(columns=['Source', 'LabelName', 'Confidence', 'XMin', 'XMax', 'YMin', 'YMax', 'IsOccluded', 'IsTruncated', 'IsGroupOf', 'IsDepiction', 'IsInside'])

# saved_csv.to_csv("./test/img_list_custom_test.csv", index=False, header=False)
saved_csv.to_csv("./test/img_list_custom_test.txt",sep=' ', index=False, header=False)


