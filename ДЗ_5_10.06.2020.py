revenue = int(input('Выручка фирмы = '))
costs = int(input('Издержки фирмы = '))
if revenue > costs:
    print('Вы отработали с прибылью')
    profitaboloty = revenue / costs * 100
    print('Ваша рентабельность', profitaboloty, '%')
elif revenue < costs:
    print('Вы отработали в убыток')
employee = int(input('Сколько сотрудников работает в фирме = '))
profit = revenue - costs
employee_profit = profit/employee
print('Прибыли на одного сотрудника', employee_profit)
