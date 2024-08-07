import pyttsx3
engine = pyttsx3.init()
running=True
while running:
    text = input("enter text to speak: ")
    engine.say(text)
        
    engine.runAndWait()
    if text=="exit":
        running=False

  

