# TTS (Text To Speech)
# 설치 : pip install gTTS, 
# pip install playsound
from gtts import gTTS
from playsound import playsound

text = '안녕하세요, 김지현입니다.'

tts = gTTS(text=text, lang='ko', slow=False)
tts.save('./studyPython/output/hi.mp3')
print('생성완료')
playsound('./studyPython/output/hi.mp3')
print('음성 출력 완료!')