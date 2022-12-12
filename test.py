import speech_recognition as sr
import os
import textwrap

CLIENTID="zqycSsvgNb1Bb4ZJgkubxw=="
CLIENTKEY="p7bbJOrZDr232RrjGxUkOzNx9pHphVDcsR6eeTw6Zp96yNYuFesaWTpcdc5pOY_3sST6dWroLak2vB1vmQ804w=="

def wavToText(filePath):
    r = sr.Recognizer()

    harvard = sr.AudioFile(filePath)
    with harvard as source:
        audio = r.record(source)
    try:
        return r.recognize_houndify(audio, client_id=CLIENTID, client_key=CLIENTKEY, show_all=True)
    except UnknownValueError:
        raise GolemException("Could not understand audio")

out = wavToText('audio_files_harvard.wav')

response = out['AllResults'][0]['WrittenResponse']

print(response)
