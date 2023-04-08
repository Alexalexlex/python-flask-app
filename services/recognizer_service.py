import speech_recognition as sr


class Recognizer:
    @staticmethod
    def recognize_speech(file_path, language_code="en-US"):
        recognizer = sr.Recognizer()

        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)

        try:
            transcript = recognizer.recognize_sphinx(
                audio_data, language=language_code)
        except sr.UnknownValueError:
            transcript = ""

        return transcript
