import speech_recognition as sr

class Mic:
    def __init__(self):
        self.CLIENTID = "zqycSsvgNb1Bb4ZJgkubxw=="
        self.CLIENTKEY = "p7bbJOrZDr232RrjGxUkOzNx9pHphVDcsR6eeTw6Zp96yNYuFesaWTpcdc5pOY_3sST6dWroLak2vB1vmQ804w=="


    def micToText(self):
        with sr.Microphone() as source:
            audio = sr.Recognizer().listen(source)
        try:
            out = sr.Recognizer().recognize_houndify(audio, client_id=self.CLIENTID, client_key=self.CLIENTKEY, show_all=True)
        except sr.UnknownValueError:
            raise sr.GolemException("Could not understand audio")
        else:
            return out['AllResults'][0]["WrittenResponse"]
        finally:
            print("Finished")
