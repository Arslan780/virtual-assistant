import pywhatkit
import random
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice to text
def take_command():
    R = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')

        R.pause_threshold = 1
        audio = R.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print('Recognizing...')
        command1 = R.recognize_google(audio, language='en-in')
        print(f'user said:{command1}')
    except Exception:
        # speak('say that again')
        return 'none'
    return command1


# to wish

def wish():
    hours = int(datetime.datetime.now().hour)

    if 0 <= hours <= 12:
        speak('good morning sir ')
    elif 12 < hours < 18:
        speak('good afternoon')
    else:
        speak('good evening sir')
    speak('The project is ready to deploy')
    speak('how can i help you')


if __name__ == '__main__':
    wish()
    while True:
        command = take_command().lower()

        if 'notepad' in command:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            speak('opening notepad')
            os.startfile(npath)
        elif 'telegram' in command:
            speak('opening telegram')
            tpath = "C:\\Users\\hp\\AppData\\Roaming\\Telegram Desktop.exe"
        elif 'whatsapp' in command:
            wpath = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\whatsapp.exe"
            speak('opening whatsapp')
            os.startfile(wpath)
        elif 'silent' in command:
            os.system("taskkill /f /im vlc.exe")
            os.system("taskkill /f /im chrome.exe")
        elif 'music' in command:
            music = "D:\\music\\Audio songs"
            speak('playing random song')
            song = os.listdir(music)
            rd = random.choice(song)
            os.startfile(os.path.join(music, rd))
        elif 'tell me about' in command:
            thing = command.replace('tell me about', '')
            info = wikipedia.summary(thing, 1)
            speak(info)
        elif 'who is' in command:
            thing = command.replace('who is', '')
            info = wikipedia.summary(thing, 1)
            speak(info)
        elif 'about' in command:
            thing = command.replace('tell me about', '')
            info = wikipedia.summary(thing, 1)
            speak(info)
        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing' + song)
            print(song)
            pywhatkit.playonyt(song)
        elif 'youtube' in command:
            speak('what do you like to play on youtube')
            print('taking command...')

            yt = take_command().lower()
            speak('opening youtube ')
            pywhatkit.playonyt(yt)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('current time is ' + time)
        elif 'info' in command:
            speak('i can open whahtsapp')
            speak('i can tell you time')
            speak('i can play songs for you')
            speak(' i can open some apps for you ')
        elif 'stop' in command:
            speak(" it's my pleasure to serve you sir ")
            speak('deactivating assistant')
            break
        elif 'close' in command:
            speak('what do you want to close')
            cl = take_command().lower()
            if 'whatsapp' in cl:
                speak('closing whatsapp')
                os.system("taskkill /f /im WhatsApp.exe")
            elif 'chrome' in cl:
                speak('closing chrome')
                os.system("taskkill /f /im chrome.exe")
            elif 'music' in cl:
                speak('closing songs')
                os.system("taskkill /f /im vlc.exe")
            elif 'song' in cl:
                speak("closing songs")
                os.system("taskkill /f /im vlc.exe")
            elif 'notepad' in cl:
                speak("closing notepad")
                os.system("taskkill /f /im notepad.exe")
        elif 'can you hear me' in command:
            speak('perfectly')
