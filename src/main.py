from audio_handler import listen, speak
from openai_integration import get_response_from_openai

def main():
    print("Jarvis Assistant démarré. Dites quelque chose...")
    while True:
        text = listen()
        if text:
            print(f"Vous avez dit: {text}")
            response = get_response_from_openai(text)
            speak(response)

if __name__ == "__main__":
    main()
    