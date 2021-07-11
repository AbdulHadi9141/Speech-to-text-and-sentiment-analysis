import speech_recognition as sr
from textblob import TextBlob
# import nltk
# nltk.download('punkt')

r = sr.Recognizer()
text = ""
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("Please say something")

    audio = r.listen(source)

    print("Recognizing Now .... ")

    try:
        text = r.recognize_google(audio)

    except Exception as e:
        print("Error :  " + str(e))

    # write audio
    with open("recorded.wav", "wb") as f:
        f.write(audio.get_wav_data())

blob = TextBlob(text)
stringPolarity = blob.polarity

print("The Sentence : " + text)
if stringPolarity > 0:
    print("is Positive")
elif stringPolarity < 0:
    print("is Negative")
elif stringPolarity == 0:
    print("is Neutral")
else:
    print("Error")
