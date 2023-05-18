import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as src:
    r.adjust_for_ambient_noise(src, duration=0.2)
    a = r.listen(src,5,3)

    t = r.recognize_google(a)
    t = t.lower()
    print(t)

