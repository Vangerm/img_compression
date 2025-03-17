import os
from PIL import Image


def compress_image(image_path, output_path, target_size_kb):
    img = Image.open(image_path)

    # Определим качество изображения
    quality = 95  # Начальное значение качества
    while os.path.getsize(output_path) > target_size_kb * 1024 and quality > 10:  # 300 КБ в байтах
        img.save(output_path, "JPEG", quality=quality)
        quality -= 5


def process_folder(folder_path, target_size_kb=300):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, filename)
                output_path = os.path.join(root, filename)

                print(f"Сжимаем изображение: {image_path}")
                compress_image(image_path, output_path, target_size_kb)
                print(f"Сохранено как: {output_path}")


if __name__ == "__main__":
    directory_to_process = input("Введите путь к папке для обработки: ")
    process_folder(directory_to_process)
