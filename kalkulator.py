def  average_grade(a,b,c):
    return (a+b+c)/3
def grade_message(average):
    if average >= 4.5:
        return "Отлично"
    elif  3.5 <= average > 4.5:
        return "Хорошо"
    else:
        return "Надо подучить"
d1 = average_grade(3,4,3)
v1 = grade_message(d1)
print(F"Средний бал {d1:.2f}.   Резултат: {v1}") #(:.2f) для вывода числа с двумя знаками после точки и не выводилась очень большая дробь
d2 = average_grade(5,4,5)
v2 = grade_message(d2)
print(F"Средний бал {d2:.2f}.   Резултат: {v2}")