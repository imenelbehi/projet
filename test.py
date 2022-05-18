import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("dit quelque chose :")
    audio = r.listen(source)
    try:
        print("you have said : " + r.recognize_google(audio, language="fr-FR"))

    except Exception as e:
        print("Error : " )


