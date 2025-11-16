from openai import OpenAI
from pathlib import Path
import os


# client = OpenAI(api_key="YOUR_API_KEY_HERE")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # أو استخدم متغير البيئة


text_file_path = Path('/Users/aymannji/Documents/04 موارد وخوارزميات وأفكار/نص إلى صوت/كتاب.txt')

with open(text_file_path, "r", encoding="utf-8") as file:
    arabic_text = file.read()

speech_file_path = Path(r"C:\Users\Aymen\Desktop\speech.mp3")

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="nova",
    input=arabic_text
)

response.stream_to_file(speech_file_path)

print("تم إنشاء ملف الصوت بنجاح:", speech_file_path)

