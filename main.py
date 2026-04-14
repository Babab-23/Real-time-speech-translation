import speech_recognition as sr
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
from deep_translator import GoogleTranslator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    fs = 16000
    seconds = 5

    print("🎤 Please speak now in English...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    write("temp.wav", fs, recording)

    recognizer = sr.Recognizer()

    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)
    try:
        print("🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""

def translate_text(text, target_language):
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        print(f"🌍 Translated text: {translated}")
        return translated
    except Exception as e:
        print(f"❌ Translation Error: {e}")
        return ""

def display_language_options():
    print("\n🌐 Available translation languages:")
    print("1. Spanish (es)")
    print("2. French (fr)")
    print("3. Arabic (ar)")
    print("4. Russian (ru)")
    print("5. Portuguese (pt)")
    print("6. Mandarin Chinese (zh-cn)")
    print("7. English (en)")
    choice = input("Select language (1-7): ")
    languages = {
        "1": "es",
        "2": "fr",
        "3": "ar",
        "4": "ru",
        "5": "pt",
        "6": "zh-cn",
        "7": "en"
    }

    return languages.get(choice, "es")

def main():
    print("=" * 40)
    print("🎙️ SPEECH TRANSLATOR")
    print("=" * 40)

    target_language = display_language_options()
    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_language)
        if translated_text:
            speak(translated_text)
            print("🔊 Translation spoken out!")

if __name__ == "__main__":
    main()