# -*- coding: utf-8 -*-
#! /usr/bin/python3
# -*- coding: utf-8 -*

# for waiting after hitting enter to not recording the enter key presses
import time

# audio recoding from
# https://gist.github.com/mabdrabo/8678538

# for recording the audio itself
import pyaudio
import wave


def oneRecording(name="lol.vaw"):

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 22050
    CHUNK = 1024
    RECORD_SECONDS = 10
    # WAVE_OUTPUT_FILENAME = "file.wav"
    WAVE_OUTPUT_FILENAME = name

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


with open('transcript_a_lire.txt','r',encoding = 'utf-8') as f:
    print("script started")


    read_data = f.read()

    lignes = read_data.split('\n')

    # print(lol1)
    #
    samples_to_do = 200

    for i in range(samples_to_do):
        ligne =  lignes[i].split('|')
        print("============================================================")
        print("\n"+str(samples_to_do)+":    read that sentence:"+ligne[1])
        print("recording into:"+ligne[0])
        filename  = ligne[0]

        oneRecording(filename)

        input("Press Enter to continue...")
        print("waiting for 1 second to not recort the enter key presses")
        time.sleep(1)



    print("script ended")



