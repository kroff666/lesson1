number = int(input('Введите целое положительно число = '))
number_max = 0
while number > 0:
    number_1 = number % 10
    if number_1 >= number_max:
        number_max = number_1
    number //= 10
print(number_max)

