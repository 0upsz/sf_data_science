def half_predict(number:int=1) -> int:
    """Угадываем число от 1 до 100 за наименьшее количество попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток 
    """
    
    count = 0 #количество попыток
    number_for_operations = 50      # число для увеличения или уменьшения диапазона
    middle = 50 # число, которое ограничивает диапазон угалываемых чисел
    
    while True:
        count+=1
        if number > middle: 
            number_for_operations = number_for_operations // 2   
            if number_for_operations == 0:
                number_for_operations = 1 
            middle = middle + number_for_operations          
            
        elif number < middle:  
            number_for_operations = number_for_operations // 2  
            if number_for_operations == 0:
                number_for_operations = 1 
            middle = middle - number_for_operations             
        else:
            break
        
    return count

def score_game(half_predict) -> int:
    """Определяет за сколько в среднем попыток компьютер угадывает 1000 чисел

    Args:
        random_predict (_func_): функция угадывания числа по диапазонам

    Returns:
        int: сколько попыток 
    """
    import numpy as np
    score_list=[] #список с количеством попыток
    np.random.seed(3)
    random_array=np.random.randint(1,100, size=1000) # список с 1000 числами
    
    for number in random_array:
        score_list.append(half_predict(number))
    score=int(np.mean(score_list))
    
    print(f'Функция угадывает каждое из 1000 чисел в среднем за {score} раз')
    return score

score_game(half_predict)