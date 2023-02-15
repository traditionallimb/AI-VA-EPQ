#! THIS IS A TEMPORARY FILE JUST AS A PLACEHOLDER TO REMIND MYSELF TO MAKE THE MIC CLASS!
import speech_recognition as sr

class Mic:

    def micToText(self, clientID, clientKey):
        with sr.Microphone() as source:
            audio = sr.Recognizer().listen(source)
        try:
            out = sr.Recognizer().recognize_houndify(audio, client_id=clientID, client_key=clientKey, show_all=True)
        except UnknownValueError:
            raise GolemException("Could not understand audio")
        else:
            print("AHGAHGAHGAHGAHGAHGAHGAHGAHG") # this line should never be executed

        return out['AllResults'][0]["WrittenResponse"]