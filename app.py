from gtts import gTTS
import os
text = "hello world"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
os.system("afplay output.mp3")