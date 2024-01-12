import speech_recognition as sr

r = sr.Recognizer()

keyword = "frost"
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    if r.recognize_houndify(audio) == keyword:
        print("Found")
except sr.UnknownValueError:
    print("Couldn't understand audio")
except sr.RequestError as e:
    print(f"Couldn't request results; {e}")



# TODO this is just a test to wait for a wake word