"""Игра Угадай Число
"""

import numpy as np

number = np.random.randint(1,101) #Загадываем число 

#количество попыток:
count=0
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100!"))
    
    if predict_number > number:
        print("число должно быть меньше!")
        
    elif predict_number < number:
        print("число должно быть больше!")
        
    else:
        print(f"Вы угадали число {number} за {count} попыток!")
        break #конец игры и выход из цикла