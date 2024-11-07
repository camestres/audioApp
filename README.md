# Description
Simple app for modifying and transcribing audiofiles.
App is able to modify speed and volume of audiofile in WAV format, and transcribe from Russian and English languages.


Modified audiofile save with suffix '_modified' at the current audiofile folder.
Transcription result write down to JSON file at the 'logs' directory.

# Clone repository:
`git clone https://github.com/yourusername/audioApp.git`   
`cd audioApp`

# Virtual environment:
`pip install -r requirements.txt`

# Install Models for transcribing
App use VOSK library with small models for transcribing.   
You need download it from:  
https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip (for RU), 
https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip (for EN) 
and put them into "models" directory manually. 

Or use these scripts for automatically installing:
`mkdir -p models/vosk-model-ru && wget -O models/vosk-model-ru/model.zip https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip && unzip models/vosk-model-ru/model.zip -d models/vosk-model-ru && rm models/vosk-model-ru/model.zip`  

`mkdir -p models/vosk-model-en && wget -O models/vosk-model-en/model.zip https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip && unzip models/vosk-model-en/model.zip -d models/vosk-model-en && rm models/vosk-model-en/model.zip`

For using large models download required models from https://alphacephei.com/vosk/models and put them into "models" directory.  
"vosk-model-ru" directory for Russian languange.   
"vosk-model-en" directory for English languange. 

# How to use 
Use command line interface in this format:   
python audioApp.py <path_to_audio_file> [--modify] [--speed <value>] [--volume <value>] [--transcribe] [--language <ru|en>]   

Description arguments:   
"speed" = 1.0 means no change   
"volume" add volume in dB   


# Examples
## Only modify 
`python audioApp.py examples/russian.wav --modify --speed 1.5 --volume 5`

## Only transcribe
`python audioApp.py examples/russian.wav --transcribe --language ru`

## Modify and transcribe
`python audioApp.py examples/english.wav --modify --speed 1.3 --volume -3 --transcribe --language en`