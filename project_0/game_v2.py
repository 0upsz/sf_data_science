"""Игра Угадай Число компьютер сам загадывает и угадывает число"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток 
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) #предполагаемое случайным образом число
        if number == predict_number:
            break # Выход из цикла если угадали
        
    return(count)

def score_game(random_predict) -> int:
      """Функция оценивает за сколько попыток в среднем испытываемая функция отгадывает число

    Args:
        random_predict (func): Функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] #создаем список, в котором будут сохранены количества попыток, с которых получилось отгадать число
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000) #создаем фиксированный список из 1000 чисел от 1 до 100
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # высчитываем среднее арифмитическое списка с количеством попыток
    print(f'Алгоритм в среднем угадывает загаданное число за {score} попыток')
    return score


if __name__ == "__main__":
    score_game(random_predict)