import os
import argparse
from modify_audio import modify_audio
from transcribe_audio import transcribe_audio
from logger import log_transcription


def main():
    parser = argparse.ArgumentParser(description="Audio Processing Application")
    parser.add_argument("audio_file", help="Path to the audio file to process")
    parser.add_argument("--modify", action="store_true", help="Modify audio (speed and volume)")
    parser.add_argument("--transcribe", action="store_true", help="Transcribe audio to text")
    parser.add_argument("--language", choices=["ru", "en"], help="Language for transcription")
    parser.add_argument("--speed", type=float, default=1.0,
                        help="Коэффициент изменения скорости воспроизведения (по умолчанию: 1.0)")
    parser.add_argument("--volume", type=float, default=0.0, help="Изменение громкости в дБ (по умолчанию: 0.0)")

    args = parser.parse_args()

    try:
        if args.modify:
            modify_audio(args.audio_file, speed=args.speed, volume=args.volume)

        if args.transcribe:
            if not args.language:
                raise ValueError("Language must be specified when transcribing.")
            transcription = transcribe_audio(args.audio_file, args.language)

            if transcription:
                print("Расшифровка:", transcription)
                log_transcription(args.audio_file, transcription, args.language)
            else:
                print("Transcription failed.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()





# def main():
#     parser = argparse.ArgumentParser(description="Аудио приложение для модификации и расшифровки аудиофайлов.")
#
#     parser.add_argument("audio_file", type=str, help="Путь к исходному аудиофайлу (WAV)")
#     parser.add_argument("--speed", type=float, default=1.0,
#                         help="Коэффициент изменения скорости воспроизведения (по умолчанию: 1.0)")
#     parser.add_argument("--volume", type=float, default=0.0, help="Изменение громкости в дБ (по умолчанию: 0.0)")
#     parser.add_argument("--language", type=str, choices=["ru", "en"], default="ru",
#                         help="Язык для распознавания (по умолчанию: ru)")
#     parser.add_argument("--output_log", type=str, default="transcription_log.json",
#                         help="Имя файла для логирования (по умолчанию: transcription_log.json)")
#
#     args = parser.parse_args()
#
#     if not os.path.exists(args.audio_file):
#         print(f"Ошибка: файл {args.audio_file} не найден.")
#         return
#
#     modified_audio = modify_audio(args.audio_file, speed=args.speed, volume=args.volume)
#     transcription = transcribe_audio(args.audio_file, language=args.language)
#     print("Расшифровка:", transcription)
#
#     log_transcription(args.audio_file, transcription, language=args.language, output_file=args.output_log)