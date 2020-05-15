import re

import speech_recognition as sr

print("sr.__version__",sr.__version__)
print("sr.__file__",sr.__file__)

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

    # generate uniqu couple that can be easily be tied with a specific audio
    dictOfUniqTwoWordsCouple = []
    allWordsCouples = []
    for sentence in strArraySentences:
        wordsFromTxt = re.split(" ",sentence)
        wordsFromTxtLen = len(wordsFromTxt)
        for wordsCoupleIndex in range(wordsFromTxtLen-1):
            tmpWordsCouple = wordsFromTxt[wordsCoupleIndex] + " " + wordsFromTxt[wordsCoupleIndex+1]
            allWordsCouples.append(tmpWordsCouple)
    for couple in allWordsCouples:
        counts = allWordsCouples.count(couple)
        # print("allWordsCouples.count(couple)",allWordsCouples.count(couple))
        # print("counts",counts)
        if(counts==1):
            print("couple is:",couple)


    # for sentence in strArraySentences:
    #     once = -1
    #     wordsFromTxt = re.split(" ",sentence)
    #     wordsFromTxtLen = len(wordsFromTxt)
    #     for w in range(wordsFromTxtLen-1):
    #         # if(wordsFromTxt[w]=="the"):
    #         #     if(wordsFromTxt[w+1]=="memorization"):
    #         #         print("if(wordsFromTxt[w+1]==memorization):")
    #         if(wordsFromTxt[w+1]=="memorization"):
    #             print("if(wordsFromTxt[w+1]==memorization):")
    #         tmpWordsCouple = wordsFromTxt[w] + " " + wordsFromTxt[w+1]
    #         print("sentence",sentence)
    #         if(tmpWordsCouple in sentence):
    #             once +=1
    #         if(once >0):
    #             print("couple rejected")
    #             continue
    #         # if(w==wordsFromTxtLen-1):
    #         #     if(once ==0):
    #         #         print("new unig couple")
    #         if(once ==0):
    #             print("new unig couple")


    audioOffsetSeconds = 56
    durationSeconds = 20

    for audioOffsetIndex in range(100):
        print('==================================')
        print("audioOffsetIndex",audioOffsetIndex)
        tmpAudioOffsetSecondsWindexStart = audioOffsetSeconds+10*audioOffsetIndex
        print("tmpAudioOffsetSecondsWindexStart",tmpAudioOffsetSecondsWindexStart)
        print("conv_sec_in_timestamp(tmpAudioOffsetSecondsWindexStart)",conv_sec_in_timestamp(tmpAudioOffsetSecondsWindexStart))
        tmpAudioOffsetSecondsWindexEnd = tmpAudioOffsetSecondsWindexStart +20
        print("tmpAudioOffsetSecondsWindexEnd",tmpAudioOffsetSecondsWindexEnd)
        print("conv_sec_in_timestamp(tmpAudioOffsetSecondsWindexEnd)",conv_sec_in_timestamp(tmpAudioOffsetSecondsWindexEnd))

        audio = r.record(source, offset=tmpAudioOffsetSecondsWindexStart, duration=20)
        print("audio extracted")
        # result = r.recognize_sphinx(audio)
        result = r.recognize_google(audio)
        print("result:",result)

        wordsFromAudio = re.split(" ",result)
        wordsFromAudioLen = len(wordsFromAudio)

        for i in range(wordsFromAudioLen-1):
            # print('testing wordsFromAudio[i],wordsFromAudio[i+1]',wordsFromAudio[i],wordsFromAudio[i+1])
            numberOfMatchedForThisI = 0
            for sentence in strArraySentences:
                # print("testing in sentence:", sentence)
                tmpTwoConsecutiveWords = wordsFromAudio[i]+" "+wordsFromAudio[i+1]
                if(tmpTwoConsecutiveWords in sentence):
                    # print("tmpTwoConsecutiveWords founded")
                    numberOfMatchedForThisI += 1
            if(numberOfMatchedForThisI!=0):
                print("numberOfMatchedForThisI",numberOfMatchedForThisI)
            # if()

        # for i in





# introduction with background music: 0:0:32
# introduction without background music: 0:0:56
