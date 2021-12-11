"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    low_number = 1
    high_number = 100
    # количество попыток
    count = 0
    print('Задуманное число', number)
    
    while low_number <= high_number:
        # Бинарный поиск: Сравниваем среднее число от макс и мин. значения с угадываемым числом
        mid = int((low_number + high_number)/2)
        count += 1
        if mid == number:
            break
        if mid > number:
            high_number = mid - 1
        else: 
            low_number = mid + 1
    print('Guess', mid, 'count', count)
    return count
    

    


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
