from PIL import Image
import os

# Ищем все файлы с расширением .gif в текущей директории
gif_files = [file for file in os.listdir('.') if file.endswith('.gif')]

# Проверяем, что найдены файлы .gif
if not gif_files:
    print('GIF files not found!')
else:
    # Обрабатываем каждый файл .gif
    for gif_path in gif_files:
        # Создаем папку для сохранения PNG-изображений текущего файла .gif
        pngs_dir = os.path.join(os.path.dirname(gif_path), f"{os.path.splitext(gif_path)[0]}_pngs")
        if not os.path.exists(pngs_dir):
            os.makedirs(pngs_dir)

        # Открываем GIF-файл
        gif_image = Image.open(gif_path)

        # Извлекаем каждый кадр из GIF-файла и сохраняем его в отдельный файл
        previous_frame = None
        frame_count = 0
        for frame in range(0, gif_image.n_frames):
            gif_image.seek(frame)
            gif_frame = gif_image.convert('RGBA')

            # Пропускаем сохранение кадра, если он идентичен предыдущему кадру
            if previous_frame and gif_frame == previous_frame:
                continue

            file_name = os.path.join(pngs_dir, f"frame_{frame_count}.png")
            gif_frame.save(file_name, format="png")

            previous_frame = gif_frame
            frame_count += 1

        # Удаляем исходный GIF-файл
        # os.remove(gif_path)
