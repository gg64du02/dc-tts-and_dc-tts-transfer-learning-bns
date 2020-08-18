
from os import path
from pydub import AudioSegment

# files
src = "ThePoetsCorner.mp3"
dst = "ThePoetsCorner.wav"
# src = "totakas-song.mp3"
# dst = "totakas-song.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")