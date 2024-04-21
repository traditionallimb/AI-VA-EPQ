import classes.recogniserClass as rc
import classes.micClass as mc
import classes.commandsClass as cc
import classes.speechClass as sc

wakeWord = "mouse"

print("Started")
mic = mc.Mic()
recognise = rc.Recognise()
commands = cc.Commands()
speech = sc.Speech()

print("Entering loop")

while True:
    print("Listening for wake word")
    wakeWordRec = mic.record("audio/wakeword.wav")
    wakeWordTxt = recognise.fileToText("audio/wakeword.wav")
    if wakeWordTxt.lower() == wakeWord:
        print("Listening for input")
        userPhraseRec = mic.record("audio/phrase.wav")
        userPhraseTxt = recognise.fileToText("audio/phrase.wav")
        print(f'"{userPhraseTxt}"')

        if userPhraseTxt.lower() in ["what is the time", "what's the time", "what time is it"]:
            response = commands.whatIsTheTime()
            speech.tts(response)
            speech.say("audio/tts.wav")
            quit()
        elif userPhraseTxt.lower() == "hello":
            print("Hello!")
            speech.say("tts.wav")
        # elif out.lower() == "":
            # print("Unable to recognise your audio")

        commands.whatIsTheWeather()
