import json
from datetime import datetime
from pathlib import Path


def log_transcription(file_name, transcription, language):
    try:
        transcription_date = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_data = {
            "file": file_name,
            "transcription_date": transcription_date,
            "language": language,
            "transcription": transcription
        }

        file_stem = Path(file_name).stem
        with open(f"logs/{file_stem}_{transcription_date}.json", 'w', encoding='utf-8') as f:
            json.dump(log_data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Ошибка при логгировании аудиофайла: {e}")
        return None