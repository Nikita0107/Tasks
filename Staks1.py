#  Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
#  Если дискриминант отрицателен, программа должна выдать ошибку
#  и предложить пользователю попробовать еще раз с другими коэффициентами.
#  При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.
import logging

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def equations(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        logger.error('Дискриминант отрицателен, уравнение не имеет корней')
        raise ValueError('Дискриминант отрицателен, уравнение не имеет корней')
    
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    
    else:
        x1 = (-b - discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        return x1, x2

while True:
    try:
        print('Введите коэффициенты для уравнения в формате: a, b, c')
        a, b, c = map(float, input().split(', '))
        
        result = equations(a, b, c)
        if len(result) > 1:
            print(f'x1 = {result[0]}, x2 = {result[1]}')
        else:
            print(f'Корень уравнения: x = {result}')
        break
    
    except ValueError as e:
        print(f'Ошибка: {e}. Попробуйте другие коэффициенты.')
        logger.error(f'Ошибка: {e}')