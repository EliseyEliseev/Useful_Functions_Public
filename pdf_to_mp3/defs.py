from gtts import gTTS
import fitz

def read_pdf(file_path):
    """Чтение текста из PDF-файла"""
    with fitz.open(file_path) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text()
        return text


def convert_to_audio(text, lang='en'):
    """Конвертация текста в аудиофайл"""
    print("Converting text to audio...")
    tts = gTTS(text=text, lang=lang)
    return tts

def save_audio_file(tts, file_path):
    """Сохранение аудиофайла"""
    print("Saving audio file...")
    tts.save(file_path)
