import re

import speech_recognition as sr

print("sr.__version__",sr.__version__)
print("sr.__file__",sr.__file__)

import sys

# ===========testing code start
import os

# List all files in a directory using os.listdir
# basepath = 'my_directory/'
basepath = 'TPC/samples/'

metadata_s_r = 'TPC/metadata_speech_recognition.csv'

for entry in os.listdir(basepath):
    # print(entry)
    if os.path.isfile(os.path.join(basepath, entry)):
        # print("====================================")
        print(entry)

        harvard = sr.AudioFile(os.path.join(basepath, entry))

        # print("harvard.filename_or_fileobject",harvard.filename_or_fileobject)

        r = sr.Recognizer()
        with harvard as source:
            tmpString = ''
            # print("source opened")
            audio = r.record(source)
            # result = r.recognize_google(audio)
            try:
                result = r.recognize_sphinx(audio)
                # print("result:",result)
                metadata_s_r_fileO = open(metadata_s_r,'a')
                tmpString = str(harvard.filename_or_fileobject) + '|' + result + '\n'
                print("tmpString:",tmpString)
                metadata_s_r_fileO.write(tmpString)
                metadata_s_r_fileO.close()
            except Exception as ex:
                print(str(ex))
                print(sys.exc_info())


exit()
# ===========testing code end

# exit()

# harvard = sr.AudioFile('harvard.wav')
# harvard = sr.AudioFile('totakas-song.wav')
harvard = sr.AudioFile('ThePoetsCorner.wav')

r = sr.Recognizer()

def timestamp_converter(hour,min,sec):
    return 3600*hour+60*min+sec

def conv_sec_in_timestamp(sec):
    return sec//3600,sec//60,sec%60



with harvard as source:
    print("source opened")
    # audio = r.record(source)
    # audio = r.record(source, duration=20)
    # audio = r.record(source, offset=120, duration=50)
    # audio = r.record(source, offset=32, duration=10)
    # audio = r.record(source, offset=timestamp_converter(0,0,32), duration=10)
    audio = r.record(source, offset=timestamp_converter(0,0,56), duration=10)
    print("audio extracted")
    # result = r.recognize_google(audio)
    # result = r.recognize_wit(audio)
    # result = r.recognize_bing(audio)
    # result = r.recognize_sphinx(audio)
    result = ""

    print("result:",result)
    fobjectTxtBook = open("B00FORPEAA_EBOK.txt", encoding='utf8')

    # strTxtBook = fobjectTxtBook.readlines()
    strTxtBook = fobjectTxtBook.read()
    # print("strTxtBook",strTxtBook)

    strSplittedTxtBook = re.split("\n",strTxtBook)
    strSplittedTxtBookWOempty =[]
    for bits in strSplittedTxtBook:
        # print("len(bits)",len(bits))
        if(len(bits)!=0):
            # print("strSplittedTxtBook bits",bits)
            # print(bits)
            strSplittedTxtBookWOempty.append(bits)
    print("len(strSplittedTxtBook)",len(strSplittedTxtBook))
    print("len(strSplittedTxtBookWOempty)", len(strSplittedTxtBookWOempty))

    strSplittedTxtBookWOemptyPointSplitted = []
    for bits in strSplittedTxtBookWOempty:
        # print("strSplittedTxtBookWOempty bits",bits)
        bit_values = re.split("\.",bits)
        for bit_value in bit_values:
            strSplittedTxtBookWOemptyPointSplitted.append(bit_value)

    print("len(strSplittedTxtBookWOemptyPointSplitted)",len(strSplittedTxtBookWOemptyPointSplitted))

    strArraySentences = strSplittedTxtBookWOemptyPointSplitted



    for sentence in strArraySentences:
        print("sentence:",sentence)

# introduction with background music: 0:0:32
# introduction without background music: 0:0:56
