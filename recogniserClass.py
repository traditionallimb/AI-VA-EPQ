import srLite as srL

class Recognise:
    def __init__(self):
        self.CLIENTID = "zqycSsvgNb1Bb4ZJgkubxw=="
        self.CLIENTKEY = "p7bbJOrZDr232RrjGxUkOzNx9pHphVDcsR6eeTw6Zp96yNYuFesaWTpcdc5pOY_3sST6dWroLak2vB1vmQ804w=="


    def fileToText(self, pathToAudio: str):
        audioFile = srL.AudioFile(pathToAudio)
        with audioFile as source:
            audio = srL.Recognizer().record(source)
        try:
            out = srL.Recognizer().recognize_houndify(audio, client_id=self.CLIENTID, client_key=self.CLIENTKEY, show_all=True)
        except srL.UnknownValueError:
            raise srL.GolemException("Could not understand audio")
        else:
            return out['AllResults'][0]["WrittenResponse"]
        finally:
            print("Finished")
