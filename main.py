import recogniserClass as rc
import micClass as mc

mic = mc.Mic()
recording = mic.record()

recognise = rc.Recognise()

out = recognise.fileToText("//wsl.localhost/Debian/home/limb/AI VA EPQ/AI-VA-EPQ/audio_files_harvard.wav") #TODO take output of microphoneClass as input
print(f'"{out}"')
