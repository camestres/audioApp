from pydub import AudioSegment

def modify_audio(file_path, speed=1.0, volume=0.0):
    try:
        audio = AudioSegment.from_wav(file_path)
        audio = audio + volume
        audio = audio.speedup(playback_speed=speed)

        modified_path = file_path.replace('.wav', '_modified.wav')
        audio.export(modified_path, format="wav")

        return modified_path

    except Exception as e:
        print(f"Ошибка при модификации аудиофайла: {e}")
        return None
