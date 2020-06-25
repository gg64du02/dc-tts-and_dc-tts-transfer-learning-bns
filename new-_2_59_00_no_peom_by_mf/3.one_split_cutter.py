from pydub.silence import detect_nonsilent
from pydub import AudioSegment



def remove_sil(path_in, path_out, format="wav"):
    sound = AudioSegment.from_file(path_in, format=format)
    print("sound",sound)
    print("sound.dBFS",sound.dBFS)
    print("sound.dBFS * 1.5",sound.dBFS * 1.5)
    # print()
    # is actually a 22050Hz file (checked with ffprobe)
    tmpAudioSegment = AudioSegment.silent(duration=1000*(6*60+31*60), frame_rate=44100)
    # return
    if(sound.duration_seconds<= 10):
        print("if(sound.duration_seconds<= 10):")
        return

    tmpSound =  AudioSegment.empty()
    # non_sil_times = detect_nonsilent(sound, min_silence_len=50, silence_thresh=sound.dBFS * 1.5)
    # non_sil_times = detect_nonsilent(sound, min_silence_len=30, silence_thresh=sound.dBFS * 1.5)
    # non_sil_times = detect_nonsilent(sound, min_silence_len=10, silence_thresh=sound.dBFS * 1.5)
    # non_sil_times = detect_nonsilent(sound, min_silence_len=10, silence_thresh=sound.dBFS * 2.25)
    # non_sil_times = detect_nonsilent(sound, min_silence_len=10, silence_thresh=sound.dBFS * 1.225)
    # non_sil_times = detect_nonsilent(sound, min_silence_len=10, silence_thresh=sound.dBFS * 3.375)
    non_sil_times = detect_nonsilent(sound, min_silence_len=10, silence_thresh=sound.dBFS * 3)
    print("detect_nonsilent done")
    # print("non_sil_times",non_sil_times)
    if len(non_sil_times) > 0:
        non_sil_times_concat = [non_sil_times[0]]
        if len(non_sil_times) > 1:
            for t in non_sil_times[1:]:
                if t[0] - non_sil_times_concat[-1][-1] < 100:
                    non_sil_times_concat[-1][-1] = t[1]
                else:
                    non_sil_times_concat.append(t)
        # non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 350]
        non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 100]
        print("non_sil_times_concat processed")
        # print("non_sil_times",non_sil_times)
        # print("len(sound)",len(sound))
        # print("non_sil_times[0][0]: non_sil_times[-1][1]",non_sil_times[0][0],non_sil_times[-1][1])
        # sound[non_sil_times[0][0]: non_sil_times[-1][1]].export(path_out)
        # print("non_sil_times[0][0]: non_sil_times[-1][1]",non_sil_times[0][0],non_sil_times[0][1])
        # sound[non_sil_times[0][0]: non_sil_times[0][1]].export(path_out)
        # index = 0

        tmpSoundBuffer = AudioSegment.empty()

        thepoetscorner_samples_counter = 0

        for int in non_sil_times:
            # tmpSound += sound[int[0]:int[1]]
            # print("tmpSoundBuffer.duration_seconds",tmpSoundBuffer.duration_seconds)

            tmpSoundBuffer = AudioSegment.empty()
            tmpSoundBuffer = sound[int[0]:int[1]]
            thepoetscorner_samples_counter += 1
            print("thepoetscorner_samples_counter",thepoetscorner_samples_counter)
            # tmpPathName = "TPC/samples2/ThePoetsCorner_2_59_00_no_peom_by_mf_{:05}.wav".format(thepoetscorner_samples_counter)
            tmpPathName = path_in[:11] + "3" + path_in[12:-4] + "_{:05}.wav".format(thepoetscorner_samples_counter)
            tmpPathName = str(tmpPathName)
            print("tmpPathName",tmpPathName)

            # making sure the end is included as well
            # tmpSound += tmpSoundBuffer

            # tmpSoundBuffer.export(tmpPathName)
            tmpSoundBuffer.export(tmpPathName, format="wav", parameters=["-ar", "22050"])
            # tmpAudioSegment.export(path_out)




            # if(tmpSoundBuffer.duration_seconds>1000):
            #     tmpSound += tmpSoundBuffer
            #     tmpSoundBuffer = AudioSegment.empty()
            #     print("if(tmpSoundBuffer.duration_seconds>1000):")
            # else:
            #     tmpSoundBuffer += sound[int[0]:int[1]]
            #     print("!if(tmpSoundBuffer.duration_seconds>1000):")
            # print("int",int)
            # print("pc",int[0]/len(sound))
            # # tmpAudioSegment[index:index+(int[1]-int[0])] = sound[int[0]:int[1]]
            # # index += int[1]-int[0]
            # # print("index",index)

        # for int in non_sil_times:
        #     # tmpSound += sound[int[0]:int[1]]
        #     print("tmpSoundBuffer.duration_seconds",tmpSoundBuffer.duration_seconds)
        #     if(tmpSoundBuffer.duration_seconds>1000):
        #         tmpSound += tmpSoundBuffer
        #         tmpSoundBuffer = AudioSegment.empty()
        #         print("if(tmpSoundBuffer.duration_seconds>1000):")
        #     else:
        #         tmpSoundBuffer += sound[int[0]:int[1]]
        #         print("!if(tmpSoundBuffer.duration_seconds>1000):")
        #     print("int",int)
        #     print("pc",int[0]/len(sound))
        #     # tmpAudioSegment[index:index+(int[1]-int[0])] = sound[int[0]:int[1]]
        #     # index += int[1]-int[0]
        #     # print("index",index)
            
        # # making sure the end is included as well
        # tmpSound += tmpSoundBuffer
        #
        # tmpSound.export(path_out)
        # # tmpAudioSegment.export(path_out)


# https://audiosegment.readthedocs.io/en/latest/audiosegment.html

# lol = 100
# tmpPathName = "samples/thepoetscorner_{:04}".format(lol)
# print("tmpPathName",tmpPathName)

import os
dir_to_process = "TPC/samples2/"
# print(os.listdir(dir_to_process))
files_list = os.listdir(dir_to_process)
for filename in files_list:
    # print("filename",filename)
    # print(os.path.join(dir_to_process, filename))
    fp_fname = os.path.join(dir_to_process, filename)
    print("fp_fname",fp_fname)

    remove_sil(fp_fname, "ThePoetsCorner_clean_2_59_00_silence-removed.wav")

exit()

remove_sil("TPC/samples/ThePoetsCorner_2_59_00_no_peom_by_mf_00034.wav", "ThePoetsCorner_clean_2_59_00_silence-removed.wav")
# remove_sil("totakas-song.wav","totakas-song_silence-removed.wav")
