'pip install pillow'
from PIL import Image

def create_sticker(input_path, output_path, sticker_size=(100, 100)):
    # Открываем изображение
    img = Image.open(input_path)

    # Создаем новое изображение для стикера
    sticker = Image.new('RGBA', sticker_size, (255, 255, 255, 0))

    # Вставляем оригинальное изображение в центр стикера
    img.thumbnail(sticker_size)
    position = ((sticker_size[0] - img.width) // 2, (sticker_size[1] - img.height) // 2)
    sticker.paste(img, position)

    # Сохраняем результат
    sticker.save(output_path, "PNG")

# Пример использования
input_image_path = "input_image.jpg"
output_sticker_path = "output_sticker.png"
create_sticker(input_image_path, output_sticker_path)


