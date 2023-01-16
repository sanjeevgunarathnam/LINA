import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("speek :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)

        print("you said : {}".format(text))
    except:
        print("sorry , couldn't get that")

