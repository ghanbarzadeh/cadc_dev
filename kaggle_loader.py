#!/usr/bin/env python

import os, sys, wget, zipfile
from pathlib import Path

if (len(sys.argv) != 2):
    print("Usage: python3 kaggle_loader.py <batch number 1-3>")
    exit(1)

if (int(sys.argv[1]) > 3) or (int(sys.argv[1]) < 1):
    print("Usage: python3 kaggle_loader.py <batch number 1-3>")
    exit(1)

run_num = int(sys.argv[1])
print(f"Run {run_num} selected.")

cadcd = [
    '2018_03_06/0001', '2018_03_06/0002', '2018_03_06/0005', '2018_03_06/0006', '2018_03_06/0008',
    '2018_03_06/0009', '2018_03_06/0010', '2018_03_06/0012', '2018_03_06/0013', '2018_03_06/0015',
    '2018_03_06/0016', '2018_03_06/0018', '2018_03_07/0001', '2018_03_07/0002', '2018_03_07/0004',
    '2018_03_07/0005', '2018_03_07/0006', '2018_03_07/0007', '2019_02_27/0002', '2019_02_27/0003',
    '2019_02_27/0004', '2019_02_27/0005', '2019_02_27/0006', '2019_02_27/0008', '2019_02_27/0009',
    '2019_02_27/0010', '2019_02_27/0011', '2019_02_27/0013', '2019_02_27/0015', '2019_02_27/0016',
    '2019_02_27/0018', '2019_02_27/0019', '2019_02_27/0020', '2019_02_27/0022', '2019_02_27/0024',
    '2019_02_27/0025', '2019_02_27/0027', '2019_02_27/0028', '2019_02_27/0030', '2019_02_27/0031',
    '2019_02_27/0033', '2019_02_27/0034', '2019_02_27/0035', '2019_02_27/0037', '2019_02_27/0039',
    '2019_02_27/0040', '2019_02_27/0041', '2019_02_27/0043', '2019_02_27/0044', '2019_02_27/0045',
    '2019_02_27/0046', '2019_02_27/0047', '2019_02_27/0049', '2019_02_27/0050', '2019_02_27/0051',
    '2019_02_27/0054', '2019_02_27/0055', '2019_02_27/0056', '2019_02_27/0058', '2019_02_27/0059',
    '2019_02_27/0060', '2019_02_27/0061', '2019_02_27/0063', '2019_02_27/0065', '2019_02_27/0066',
    '2019_02_27/0068', '2019_02_27/0070', '2019_02_27/0072', '2019_02_27/0073', '2019_02_27/0075',
    '2019_02_27/0076', '2019_02_27/0078', '2019_02_27/0079', '2019_02_27/0080', '2019_02_27/0082'
]

files_per_run = 25
for i in range((run_num - 1)*files_per_run, (run_num)*files_per_run):
    file_name = cadcd[i]
    base_url = 'http://wiselab.uwaterloo.ca/cadcd_data/' + file_name
    print(base_url)
    

# for date in dates:
#     print(date)
#     date_path = dataset_path + '/cadcd/' + date
#     date_dir = Path(date_path)
#     date_dir.mkdir(parents=True, exist_ok=True)

#     # Download calibration for this date
#     os.chdir(date_path)
#     calib_url = 'http://wiselab.uwaterloo.ca/cadcd_data/' + date + '/calib.zip'
#     calib_filename = wget.download(calib_url)
#     # Extract files
#     zip = zipfile.ZipFile(calib_filename)
#     zip.extractall()
#     zip.close()
#     # Delete zip file
#     os.remove(calib_filename)

#     for drive in cadcd[date]:
#         print(drive)
#         drive_path = dataset_path + '/cadcd/' + date + '/' + drive
#         drive_dir = Path(drive_path)
#         drive_dir.mkdir(parents=True, exist_ok=True)

#         # Download drive
#         os.chdir(drive_path)
#         base_url = 'http://wiselab.uwaterloo.ca/cadcd_data/' + date + '/' + drive
#         if labeled:
#             data_url = base_url + '/labeled.zip'
#             ann_3d_url = base_url + '/3d_ann.json'
#             ann_3d_filename = wget.download(ann_3d_url)
#         else:
#             data_url = base_url + '/raw.zip'
#         data_filename = wget.download(data_url)

#         # Extract files
#         zip = zipfile.ZipFile(data_filename)
#         zip.extractall()
#         zip.close()

#         # Delete zip file
#         os.remove(data_filename)
