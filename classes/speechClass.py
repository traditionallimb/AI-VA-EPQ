from gtts import gTTS
import pyaudio
import wave
from pydub import AudioSegment


class Speech:
    def __init__(self):
        self.__chunk = 1024

    def tts(self, stringToSay):
        vocalised = gTTS(text=stringToSay, lang='en', slow=False)
        vocalised.save("audio/tts.mp3")
        revocalised = AudioSegment.from_mp3("audio/tts.mp3")
        revocalised.export("audio/tts.wav", format="wav")

    def say(self, audioFile):
        filename = audioFile
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(self.__chunk)

        while data != '':
            stream.write(data)
            data = wf.readframes(self.__chunk)

        stream.close()
        p.terminate()
