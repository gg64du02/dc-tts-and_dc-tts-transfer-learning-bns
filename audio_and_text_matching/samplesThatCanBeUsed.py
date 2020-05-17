
import os


# basepath = 'TPC/samples/'
#
# for entry in os.listdir(basepath):
#     # print(entry)
#     if os.path.isfile(os.path.join(basepath, entry)):
#         # print("====================================")
#         print(entry)


listSpeechRecognized = ""

metadata_fO_path = "TPC/metadata_speech_recognition.csv"

metadata_fO = open(metadata_fO_path,"r")

import re

import shutil

metadata_fO_str = metadata_fO.read()

print("metadata_fO_str",metadata_fO_str)

metadata_fO_array = re.split('\n',metadata_fO_str)

print("metadata_fO_array",metadata_fO_array)

for fileStr in metadata_fO_array:
    filePathStr = re.split('\|',fileStr)
    print("filePathStr",filePathStr)

    targetCopyStr = str(str(filePathStr[0][0:11])+'2'+str(filePathStr[0][11:36]))
    print("targetCopyStr",targetCopyStr)

    shutil.copyfile(filePathStr[0], targetCopyStr)



