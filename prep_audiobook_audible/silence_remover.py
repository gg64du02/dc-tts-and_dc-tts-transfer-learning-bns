from pydub.silence import detect_nonsilent
from pydub import AudioSegment



def remove_sil(path_in, path_out, format="wav"):
    sound = AudioSegment.from_file(path_in, format=format)
    print("sound",sound)
    # print()
    # tmpAudioSegment = AudioSegment.silent(duration=1000*(6*60+31*60), frame_rate=44100)
    # return

    tmpSound =  AudioSegment.empty()
    # non_sil_times = detect_nonsilent(sound, min_silence_len=50, silence_thresh=sound.dBFS * 1.5)
    # non_sil_times = detect_nonsilent(sound, min_silence_len=30, silence_thresh=sound.dBFS * 1.5)
    non_sil_times = detect_nonsilent(sound, min_silence_len=10, silence_thresh=sound.dBFS * 1.5)
    print("non_sil_times",non_sil_times)
    if len(non_sil_times) > 0:
        non_sil_times_concat = [non_sil_times[0]]
        if len(non_sil_times) > 1:
            for t in non_sil_times[1:]:
                if t[0] - non_sil_times_concat[-1][-1] < 200:
                    non_sil_times_concat[-1][-1] = t[1]
                else:
                    non_sil_times_concat.append(t)
        # non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 350]
        non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 100]
        print("non_sil_times",non_sil_times)
        print("len(sound)",len(sound))
        print("non_sil_times[0][0]: non_sil_times[-1][1]",non_sil_times[0][0],non_sil_times[-1][1])
        # sound[non_sil_times[0][0]: non_sil_times[-1][1]].export(path_out)
        # print("non_sil_times[0][0]: non_sil_times[-1][1]",non_sil_times[0][0],non_sil_times[0][1])
        # sound[non_sil_times[0][0]: non_sil_times[0][1]].export(path_out)
        for int in non_sil_times:
            tmpSound += sound[int[0]:int[1]]
            print("int",int)
        tmpSound.export(path_out)

# https://audiosegment.readthedocs.io/en/latest/audiosegment.html

# remove_sil("ThePoetsCorner.mp3", "ThePoetsCorner_silence-removed.wav.mp3")
remove_sil("totakas-song.wav","totakas-song_silence-removed.wav")
