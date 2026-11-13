# Задача 4. Точка не лежит на осях. Определить номер четверти.

x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
    print("I четверть")
elif x < 0 and y > 0:
    print("II четверть")
elif x < 0 and y < 0:
    print("III четверть")
else:
    print("IV четверть")        # остаётся только x > 0, y < 0