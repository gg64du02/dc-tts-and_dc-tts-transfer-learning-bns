
import speech_recognition as sr

print("sr.__version__",sr.__version__)

# harvard = sr.AudioFile('harvard.wav')
# harvard = sr.AudioFile('totakas-song.wav')
harvard = sr.AudioFile('ThePoetsCorner.wav')

r = sr.Recognizer()

with harvard as source:
    # audio = r.record(source)
    # audio = r.record(source, duration=20)
    audio = r.record(source, offset=120, duration=50)
    print("")
    result = r.recognize_google(audio)
    # result = r.recognize_wit(audio)
    # result = r.recognize_bing(audio)
    # result = r.recognize_sphinx(audio)
    print("result",result)
