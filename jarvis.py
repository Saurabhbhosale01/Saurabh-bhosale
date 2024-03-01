import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    rate = engine.getProperty('rate')

    engine.setProperty('rate',130)

    engine.say(text)
    
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("saurabh said:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError as e:
            print("sorry i didn't get that. ; {0}".format(e))
            return ""
def perform_action(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    elif "who created you" in command:
        speak(f"mr.saurabh bhosale created me.......")
    elif "who is sourabh bhosale" in command:
        speak(f"mr.saurabh bhosale created me he belongs to kallamb and currently persuing btech in n b n s c o e he completed his 10 in vidhya bhavan high school kallamb he completed his 12 in v p college baramati ")
    elif "who is nikhil ghodke" in command:
        speak(f"mr. nikhil ghodke is a topper of e n t c department ")
    elif "how are you" in command:
        speak(f" i am fine whats about you")
    elif "who is your girlfriend" in command:
        speak(f" mai nahi bataunga")
    elif "what is your date of birth" in command:
        speak(f"i have no any birth day saurabh create me on fifteen feb two thousand twentyfour")
    elif "search" in command:
        speak("What would you like me to search for?")
        search_query = listen()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}")
    elif "exit" in command:
        speak("nice to meet you Goodbye!")
        exit()
    else:
        speak("Sorry, I couldn't understand that.")
def main():
    speak("Hello!saurabh. i am jarvis")
    while True:
        command = listen()
        if command:
            perform_action(command)

if __name__ == "__main__":
    main()
