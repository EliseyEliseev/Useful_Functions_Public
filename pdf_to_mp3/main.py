import time
from tqdm import tqdm
from defs import read_pdf, convert_to_audio, save_audio_file

def main():
    # Выбор языка
    lang = input("Enter language code (default is 'en'): ") or 'en'

    # Путь к PDF-файлу
    file_path = input(r"Enter PDF file path: ")

    # Чтение текста из PDF-файла
    print("Reading PDF file...")
    text = read_pdf(file_path)

    # Конвертация текста в аудиофайл
    tts = convert_to_audio(text, lang)

    # Сохранение аудиофайла
    save_audio_file(tts, 'output.mp3')

if __name__ == '__main__':
    # Инициализация прогресс-бара
    with tqdm(total=100, desc="Loading...", unit=" %") as progress_bar:
        for i in range(10):
            time.sleep(0.3)
            progress_bar.update(10)
    main()
