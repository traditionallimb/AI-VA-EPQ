import speech_recognition as sr

CLIENTID="zqycSsvgNb1Bb4ZJgkubxw=="
CLIENTKEY="p7bbJOrZDr232RrjGxUkOzNx9pHphVDcsR6eeTw6Zp96yNYuFesaWTpcdc5pOY_3sST6dWroLak2vB1vmQ804w=="



sr.Microphone()

def mic_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = r.listen(source)
    try:
        return r.recognize_houndify(audio, client_id=CLIENTID, client_key=CLIENTKEY, show_all=True)
    except UnknownValueError:
        raise GolemException("Could not understand audio")
    else:
        print("AGHHGHAGHAGAHGAHGAHGAHGAHGAGH") # theoretically this line should never be used

out = mic_to_text()

response = out['AllResults'][0]["WrittenResponse"]

print(response)

#TODO turn all of this into a class to be called in the main program