#Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a+b)%2==(c+b)%2:
    print("No")
else:
    print("Yes")
