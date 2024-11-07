from vosk import Model, KaldiRecognizer
import wave
import json

def transcribe_audio(file_path, language="ru"):
    try:
        model_path = f"models/vosk-model-{language}"  # папка с моделью для языка
        model = Model(model_path)

        wf = wave.open(file_path, "rb")
        recognizer = KaldiRecognizer(model, wf.getframerate())

        transcription = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                transcription += result.get("text", "") + " "

        final_result = json.loads(recognizer.FinalResult())
        transcription += final_result.get("text", "")

        return transcription.strip()

    except Exception as e:
        print(f"Ошибка при расшифровке аудиофайла: {e}")
        return None