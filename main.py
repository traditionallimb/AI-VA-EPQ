import recogniserClass as rc
import micClass as mc
import commandsClass as cc
import speechClass as sc

print("Started")
mic = mc.Mic()
recording = mic.record()
recognise = rc.Recognise()
commands = cc.Commands()
speech = sc.Speech()

out = recognise.fileToText("recorded.wav")
print(f'"{out}"')

if out.lower() == "what is the time":
    response = commands.whatIsTheTime()
    speech.tts(response)
    speech.say("tts.wav")
