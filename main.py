import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import news
# from openai import OpenAI 

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c): 
    print(f"Received command: {c}")
    c = c.lower()
    if "open google"in c:
        webbrowser.open("https://google.com")

    elif "open linkedin"in c:
        webbrowser.open("https://linkedin.com")

    elif "open youtube"in c:
        webbrowser.open("https://youtube.com")

    elif c.startswith("play "):
        song = c[len("play "):].strip()  # Extract the song title
        print(f"Song to play: {song}")  # Debugging
        
        # Ensure 'song' is a string and check the music library for this song
        if isinstance(song, str):
            try:
                link = musicLibrary.music[song]
                print(f"Found link: {link}")  # Debugging
                webbrowser.open(link)
            except KeyError:
                print(f"Song '{song}' not found in music library")  # Debugging
                speak("Sorry, I couldn't find that song.")
        else:
            print("Error: 'song' is not a string")  # Debugging
            speak("An error occurred while processing the song title.")

    elif c.startswith("show "):
        info = c[len("show "):].strip()  # Extract the type of news
        print(f"News to shown: {info}")  # Debugging

        # Ensure 'info' is a  string and check the music library for this song
        if isinstance(info, str):
            try:
                link = news.news[info]
                print(f"Found link: {link}") # Debugging
                webbrowser.open(link)
            except KeyError:
                print(f"News '{info}' not found in music library") # Debugging
                speak("Sorry, I couldn't find that news.")
        else:
            print("Error: 'news' is not a string") # Debugging
            speak("An error occured while processing the type of news")


if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
