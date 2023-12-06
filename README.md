import nltk
import random

nltk.download('punkt')

# Загружаем данные для обучения
responses = {
    "привет": ["Привет!", "Привет, как дела?", "Здравствуй!"],
    "как дела": ["Хорошо, спасибо!", "Не плохо, а у тебя?", "Отлично!"],
    "пока": ["Пока!", "До свидания!", "До встречи!"],
    "погода": ["Погода отличная!", "Дождливо сегодня.", "Солнечно и тепло."],
    "помощь": ["Я чат-бот. Просто напиши мне что-то!"]
}

def get_response(message):
    # Приводим сообщение к нижнему регистру
    message = message.lower()

    # Разбиваем сообщение на слова
    words = nltk.word_tokenize(message)

    # Поиск ключевого слова в сообщении
    for key_word in responses:
        if key_word in words:
            return random.choice(responses[key_word])

    # Если ключевое слово не найдено, возвращаем случайный ответ
    return "Не понимаю тебя. Может быть, попробуешь что-то еще?"

# Простой цикл для общения с ботом
while True:
    user_input = input("Ты: ")
    if user_input.lower() == "выход":
        print("До свидания!")
        break
    response = get_response(user_input)
    print("Бот:", response)
