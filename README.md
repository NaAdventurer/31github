ола

# Простой цикл для общения с ботом
while True:
    user_input = input("Ты: ")
    if user_input.lower() == "выход":
        print("До свидания!")
        break
    response = get_response(user_input)
    print("Бот:", response)
