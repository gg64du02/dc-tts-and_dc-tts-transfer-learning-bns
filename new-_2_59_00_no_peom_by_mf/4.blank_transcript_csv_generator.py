from pydub.silence import detect_nonsilent
from pydub import AudioSegment


# https://audiosegment.readthedocs.io/en/latest/audiosegment.html

# lol = 100
# tmpPathName = "samples/thepoetscorner_{:04}".format(lol)
# print("tmpPathName",tmpPathName)

file_transcript_csv = "TPC/transcript.csv"

import os
dir_to_process = "TPC/samples3/"
# print(os.listdir(dir_to_process))
files_list = os.listdir(dir_to_process)


f = open(file_transcript_csv,"w+")


for filename in files_list:
    # print("filename",filename)
    # print(os.path.join(dir_to_process, filename))
    # print(filename[55:])
    if(filename[55:]!="wav"):
        continue
    fp_fname = os.path.join(dir_to_process, filename)
    print("fp_fname",fp_fname)

    sound = AudioSegment.from_file(fp_fname, format="wav")

    durAtion = round(sound.duration_seconds, 2)
    print("durAtion", durAtion)
    tmpStr = fp_fname+"|"+str(durAtion)+'|'+'\n'

    f.write(tmpStr)

    # remove_sil(fp_fname, "ThePoetsCorner_clean_2_59_00_silence-removed.wav")

f.close()

exit()

