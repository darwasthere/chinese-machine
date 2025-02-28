import googletrans
import speech_recognition
import gtts
import playsound
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="bg")
    print(text)


translator = googletrans.Translator()
translation = translator.translate(text,dest="en")
print (translation.text)
converted_audio = gtts.gTTS(translation.text, lang="en")
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")