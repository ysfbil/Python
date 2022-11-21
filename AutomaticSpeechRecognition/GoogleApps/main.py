import os
import random
import time
import webbrowser

from playsound import playsound
import wikipedia
import speech_recognition as sr
from gtts import gTTS

wikipedia.set_lang('TR')
r=sr.Recognizer()

devam=True


'''for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))'''


def record_audio(ask=False):
    if ask:
        #print(ask)
        aispeak(ask)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)
        # audio=r.record(source,duration=3)
        try:
            voice_data = r.recognize_google(audio, language='TR-tr')
            print('Tanınan metin: ',voice_data)
        except sr.UnknownValueError:
            voice_data='?'
            print("anlayamadım efendim!")
        except sr.RequestError:
            voice_data='?'
            print("Sistem hatası")
        return voice_data

def respond(voice_data):
    if "ara" in voice_data:
        s=record_audio('aramamı istediğiniz kelimeyi söyleyin')
        url='https://www.google.com/search?q='+s
        aispeak(s+' internette aranıyor.')
        webbrowser.get().open(url)
    elif "bilgi" in voice_data:
        try:
            s=record_audio('Hangi konuda bilgi istersiniz?')
            wikikelime=wikipedia.summary(s,sentences=1)
            print(wikikelime)
            aispeak(wikikelime)
        except wikipedia.PageError:
            print('kelime bulunamadı')
        except wikipedia.DisambiguationError as e:
            print(e)
    elif "kere" in voice_data.lower():
        s = voice_data.split("kere", maxsplit=1)
        if (len(s)>1):
            s1=int(s[0])
            s2=int(s[1])
            son=str(s1*s2)
            print('Sonuç: ',son)
            aispeak(son+' eder.')
        else:
            print(s)

    elif "çıkış" in voice_data.lower():
        global  devam
        aispeak('Görüşmek üzere')
        devam=False


def aispeak(auidio_string):
    tts=gTTS(text=auidio_string,lang='tr')
    r=random.randint(1,100000)
    audio_file="audio_"+str(r)+".mp3"
    tts.save(audio_file)
    time.sleep(1)
    playsound(audio_file)
    print(auidio_string)
    os.remove(audio_file)



time.sleep(1)

print('Çıkmak için "Çıkış" söyleyin')

while devam:
    aispeak("Emriniz nedir?")
    voice_data=record_audio()
    respond(voice_data)



