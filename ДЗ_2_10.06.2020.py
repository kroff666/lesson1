data = int(input('Second='))
hour = data/3600
second = (data//60)%60
minute = (data/60)%60

print(int(hour),':',int(minute),':',int(second))
