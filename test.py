import speech_recognition as sr
import os

CLIENTID="zqycSsvgNb1Bb4ZJgkubxw=="
CLIENTKEY="p7bbJOrZDr232RrjGxUkOzNx9pHphVDcsR6eeTw6Zp96yNYuFesaWTpcdc5pOY_3sST6dWroLak2vB1vmQ804w=="

r = sr.Recognizer()

harvard = sr.AudioFile('audio_files_harvard.wav')
with harvard as source:
    audio = r.record(source)

print(r.recognize_houndify(audio, client_id=CLIENTID, client_key=CLIENTKEY))
