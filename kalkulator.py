def  average_grade(a,b,c):
    return (a+b+c)/3
def grade_message(average):
    if average >= 4.5:
        return "Отлично"
    elif  3.5 <= average >= 4.5:
        return "Хорошо"
    else:
        return "Надо подучить"
d = average_grade(3,4,3)
v = grade_message(d)
print(F"Средний бал {d:.2f}.   Резултат: {v}") #(:.2f) для вывода числа с двумя знаками после точки и не выводилась очень большая дробь