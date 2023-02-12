def middle_predict(number:int=1) -> int:
    """Функция по угадыванию числа с минимально возможного количества попыток

    Args:
        number (int, optional): загадываемое число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0 # вводим счетчик
    a = 0 # левая граница диапазона загадываемого числа
    b = 101 # правая граница диапазона загадываемого числа
    middle = (a+b)//2 # ередина диапазона, округляется до целого значения до запятой
    
    while True: # вход в цикл и последовательное уменьшения краев диапазона до момента, когда загаданное число совпадет с серединой диапазона
        count+=1
        
        if number < middle:
            b=middle
            middle = (a+b)//2
            
        elif number > middle:
            a=middle   
            middle = (a+b)//2  
            
        elif number == middle: # условие выхода из цикла
            break
    return count
    
def score_game(middle_predict) -> int:
    """Определяет за сколько в среднем попыток компьютер угадывает 1000 чисел

    Args:
        middle_predict (function): Оцениваемая функция

    Returns:
        int: Среднее количество попыток угадывания
    """

    count_ls = [] # список c кол-ом попыток угадывания
    import numpy as np
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size =(1000)) # создаем массив из 1000 загаданных чисел 
    
    for number in random_array:
        count_ls.append(middle_predict(number))
        score = int(np.mean(count_ls))
    print(f'Ваш алгоритм в среднем угадывает число за {score} попыток')

#RUN    
score_game(middle_predict)