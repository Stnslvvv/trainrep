import random

def get_user_choice():
    """Функция для получения выбора пользователя."""
    while True:
        user_input = input("Выберите: камень, ножницы или бумага: ").strip().lower()
        if user_input in ["камень", "ножницы", "бумага"]:
            return user_input
        else:
            print("Неверный ввод. Попробуйте еще раз.")

def get_computer_choice():
    """Функция для получения случайного выбора компьютера."""
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user_choice, computer_choice):
    """Функция для определения победителя."""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    """Основная функция для запуска игры."""
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nВаш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

# Запуск игры
play_game()