money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
money = money_capital  # денег в самом начале
delta = money - spend  # разница между имеющимися деньгами и тратами

while delta > 0:
    money = delta + salary
    month += 1
    spend *= (1 + increase)
    delta = money - spend

print(month)
