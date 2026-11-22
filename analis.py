def  analyze_scores(*scores):
    if not scores:#Для тоо что бы при отсутствии не возникало проблем с делением на ноль задаем условие что если аргуметов нету все три результата автоматически равны нулям
        return 0,0,0
    a = sum(scores)
    b = len(scores)
    c = a / b
    return a, b, c
a1,b1,c1 = analyze_scores(8,10,7,9)
print(f"Сумма: {a1}, Количество: {b1}, Среднее: {c1}")
a2,b2,c2 =  analyze_scores(5,5)
print(f"Сумма: {a2}, Количество: {b2}, Среднее: {c2}")
a3,b3,c3 =  analyze_scores()
print(f"Сумма: {a3}, Количество: {b3}, Среднее: {c3}")
def print_report(team_name, **info):
    print(f"Команда: {team_name}")
    for key, value in info.items():
        print(f"{key}: {value}")
print_report("Комета", Группа = "ФА261", Капитан ="Дими") 