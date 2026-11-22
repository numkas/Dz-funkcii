def ticket_total(count, price=12):
    return count * price
def final_price(count, is_school_group=False):
    total = ticket_total(count)
    if is_school_group:
        return total * 0.75
    return total
a = final_price(3)
print(f"Итоговая цена: {a}")
b = final_price(4, is_school_group=True)
print(f"Итоговая цена (с учетом скидки для школьников): {b}")
c = ticket_total(2, price=15) #Так как мы задаём новую цену то мы вызываем первую функцию ticket_total для изменения цены 
print(f"Итогоая цена (с учетом измененной ценв): {c}")