# Домашнє завдання:
# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.


def arithmetic_progression(res):
    step = res[1] - res[0]
    next_step_arith = res[-1] + step
    return next_step_arith


def geo_progression_2(res):
    next_step_geo_2 = res[-1] * 2
    return next_step_geo_2


def square_number(res):
    square_step = (len(res) + 1) ** 2
    return square_step


seq = input('>>>')
seq = seq.split()
res = [int(num) for num in seq]

is_arithmetic = all(res[i] - res[i-1] == res[1] - res[0] for i in range(1, len(res)))
is_geometric = res[1] % res[0] == 0 and all(res[i] / res[i-1] == res[1] / res[0] for i in range(1, len(res)))
def is_square_sequence(res):
    i = 1
    while i**2 <= res[-1]:
        if i**2 in res:
            i += 1
        else:
            return False
    return True




if is_arithmetic:
    print('it is arithmetic progression and next digit is=', arithmetic_progression(res))
elif is_geometric:
    print('it is geometric progression and next digit is=', geo_progression_2(res))
elif is_square_sequence is not True:
    print('it is square progression and next digit is=', square_number(res))
else:
    print('seq error')






# Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99. Знайдіть найбільший паліндром,
# одержаний множенням двох трицифрових чисел. Виведіть значення цього паліндрому і те, множенням яких чисел він є.

def max_polindrome():
    polindrome = 0
    num1 = 0
    num2 = 0
    for i in range(900, 1000):
        for k in range(900, 1000):
            res = i * k
            if str(res) == str(res)[::-1]:
                if res > polindrome:
                    polindrome = res
                    num1 = i
                    num2 = k
    return polindrome, num1, num2


print(max_polindrome())

