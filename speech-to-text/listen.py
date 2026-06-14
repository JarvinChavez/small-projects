import sys
import signal
import speech_recognition as sr


def _graceful_exit(signum, frame):
    print("\nStopping listener…")
    sys.exit(0)


def main() -> None:
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Calibrating for ambient noise (1s)…")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ready. Speak! Press Ctrl+C to stop.")

            while True:
                print("Listening…")
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio)
                    print(f"You said: {text}")
                except sr.UnknownValueError:
                    print("Didn't catch that.")
                except sr.RequestError as err:
                    print(f"Recognition service error: {err}")
    except OSError as err:
        print(f"Microphone error: {err}")
        sys.exit(1)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, _graceful_exit)
    main()
