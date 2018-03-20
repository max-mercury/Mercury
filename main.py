import sys

import yaml
import speech_recognition as sr

from brain import brain
from GreyMatter.SenseCells.tts import tts
from GreyMatter import play_music

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

#Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
proxy_username = profile_data['proxy_username']
proxy_password = profile_data['proxy_password']
music_path = profile_data['music_path']

play_music.mp3gen(music_path)


tts('Welcome' + name + ',systems are now ready to run. How can I help you?')

def main():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)  # here
        print("Say Something!")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'","")
        #speech_text = r.recognize_google(audio)
        print("Mercury thinks you said '" + speech_text + "'")
        #tts(speech_text)
        brain(name,speech_text,music_path,city_name,city_code,proxy_username,proxy_password)
    except sr.UnknownValueError:
        print("Mercury could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speecg Recognitionservice;{0}".format(e))


main()
