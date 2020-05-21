import re

import speech_recognition as sr

print("sr.__version__",sr.__version__)
print("sr.__file__",sr.__file__)

import sys

# ===========testing code start
import os

# List all files in a directory using os.listdir
# basepath = 'my_directory/'
basepath = 'data/TPC/samples/'

metadata_s_r = 'data/transcript.csv'

metadata_s_r_patched = 'data/transcript_patched.csv'


fo_transcript_csv = open(metadata_s_r,'r')
fo_transcript_csv_content = fo_transcript_csv.read()

fo_content_list = re.split("\n",fo_transcript_csv_content)
print("len(fo_content_list)",len(fo_content_list))
for line in fo_content_list:
    # print("line",line)
    sa = re.split("\|",line)
    fn = sa[0]
    text = sa[1]
    # print(fn)
    # print(text)
    entry = fn
    # harvard = sr.AudioFile(os.path.join(basepath, entry))
    harvard = sr.AudioFile(os.path.join("data/",entry))
    r = sr.Recognizer()
    with harvard as source:
        audio = r.record(source)
        durAtion = round(len(audio.frame_data)/(audio.sample_rate*audio.sample_width),2)
        print("durAtion",durAtion)
        result = text
        tmpString = str(harvard.filename_or_fileobject) + '|' + result +'|' + result + '|' + str(durAtion) +'\n'
        print("tmpString",tmpString)
        fo_transcript_csv_patched = open(metadata_s_r_patched,'a')
        fo_transcript_csv_patched.write(tmpString)
        fo_transcript_csv_patched.close()


exit()
