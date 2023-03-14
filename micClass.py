import pyaudio
import wave

class Mic:
    def __init__(self):
        self.__chunk = 1024  # Record in chunks of 1024 samples
        self.__sampleFormat = pyaudio.paInt16  # 16 bits per sample
        self.__channels = 2
        self.__fs = 44100  # Record at 44100 samples per second
        self.__seconds = 3
        self.__filename = "output.wav"

    def record(self) -> 'audio file':
        p = pyaudio.PyAudio()  # Create an interface to PortAudio

        print("Recording")

        stream = p.open(format=self.__sampleFormat,
                        channels=self.__channels,
                        rate=self.__fs,
                        frames_per_buffer=self.__chunk,
                        input=True)
        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(self.__fs / self.__chunk * self.__seconds)):
            data = stream.read(self.__chunk)
            frames.append(data)

        # Stop and close the steam
        stream.stop_stream()
        stream.close()
        # Terminate the interface
        p.terminate()

        print("Finished recording")

        # Save the recorded data as a WAV file
        wf = wave.open(self.__filename, 'wb')
        wf.setnchannels(self.__channels)
        wf.setsampwidth(p.get_sample_size(self.__sampleFormat))
        wf.setframerate(self.__fs)
        wf.writeframes(b''.join(frames))
        wf.close()