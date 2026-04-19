import speech_recognition as sr
from googletrans import Translator

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def listen_and_translate(source_lang='en', target_lang='es'):
    with sr.Microphone() as source:
        print("🎤 Listening... Speak now")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)
            print("🧠 Recognizing...")

            text = recognizer.recognize_google(audio, language=source_lang)
            print(f"🗣 You said: {text}")

            translated = translator.translate(text, src=source_lang, dest=target_lang)
            print(f"🌍 Translated ({target_lang}): {translated.text}")

        except sr.WaitTimeoutError:
            print("⏱ No speech detected.")
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except sr.RequestError:
            print("⚠ API error. Check internet connection.")

if __name__ == "__main__":
    print("=== Real-Time Speech Translator ===")

    source_lang = input("Enter source language (e.g. en, fr, es): ").lower()
    target_lang = input("Enter target language (e.g. en, fr, es): ").lower()

    while True:
        listen_and_translate(source_lang, target_lang)

        cont = input("Press Enter to continue or type 'q' to quit: ")
        if cont.lower() == 'q':
            break