import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# # cycles through all available voices in the computer registry, make sure to install appropriate language packages
# # only used for testing purposes, comment this code when not needed
# for voice in voices:
#     print(voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say('Hello Ian')
# engine.runAndWait()

listener = sr.Recognizer()

engine.say('Hello Ian')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.say('What can I do for you?')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'colonel' in command:
                command = command.replace('colonel', '')
                print(command)
    except:
        pass
    return command


# All if and elif commands need to be written in lower-case format without any special characters (!,?)
def run_colonel():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '' + '?')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'can you hear me' in command:
        talk("Yes, Ian. Age hasn't slowed you down one bit")
    elif 'can i succeed' in command:
        talk('Yes Ian, I believe you will succeed!')
    elif 'what is love' in command:
        talk('I can not compute.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I did not get that, please repeat the command again.')

# loop will execute again and again to keep the AI running, until user manually shuts down the process


while True:
    run_colonel()

