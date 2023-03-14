import recogniserClass as rc
import micClass as mc

mic = mc.Mic()
recording = mic.record()

recognise = rc.Recognise()

out = recognise.fileToText("output.wav")
print(f'"{out}"')
