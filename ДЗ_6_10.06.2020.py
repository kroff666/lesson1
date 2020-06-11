day_1 = int(input('Сколько километров пробежал за первый день '))
the_end = int(input('Всего пробежал км '))
i = 1.1
while day_1 < the_end:
    print("{:.2f}".format(day_1))
    day_1 = day_1 * i
print("{:.0f}".format(day_1))
print('Ответ: на -й день спортсмен достиг результата — не менее', the_end, 'км')