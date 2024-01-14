import classes.recogniserClass as rc
import classes.micClass as mc
import classes.commandsClass as cc
import classes.speechClass as sc

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
#elif out.lower() == "":
    #print("Unable to recognise your audio")
