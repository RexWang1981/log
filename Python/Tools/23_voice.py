import pyttsx3
def onStart(name):
   print ('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('Be careful when you send email out, always check if there is error, if the person you are trying to send to are correct people..')
engine.runAndWait()