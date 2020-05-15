
import speech_recognition as sr

print("sr.__version__",sr.__version__)
print("sr.__file__",sr.__file__)

# exit()

# harvard = sr.AudioFile('harvard.wav')
# harvard = sr.AudioFile('totakas-song.wav')
harvard = sr.AudioFile('ThePoetsCorner.wav')

r = sr.Recognizer()

def timestamp_converter(hour,min,sec):
    return (3600*hour+60*min+sec)

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
    result = r.recognize_sphinx(audio)
    print("result",result)


# introduction with background music: 0:0:32
# introduction without background music: 0:0:56
