# Задача 1. Космическая еда
# Ваш космический корабль потерпел крушение на пустынной планете. Еды здесь нет, но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться, то у вас будет уходить по четыре килограмма гречки в месяц.

# Что нужно сделать
# Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том, сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится. Используйте цикл for.

# Пример
# Информация о запасах гречки:
# Через 1 месяц: 96 кг гречки в запасе
# Через 2 месяц: 92 кг гречки в запасе
# Через 3 месяц: 88 кг гречки в запасе
# …
# …
# …
# Через 25 месяц: 0 кг гречки в запасе

# Запасы гречки закончились.

print("Информация о запасах гречки:")
for month in range(1, 26):
    remaining = 100 - 4 * month
    print(f"Через {month} месяц: {remaining} кг гречки в запасе")
print("\nЗапасы гречки закончились.")

# ======================================================================================================================================

# Объяснение:

# Инициализация цикла:

# range(1, 26) создаёт последовательность от 1 до 25 (включительно), так как запас гречки закончится через 25 месяцев (100 кг / 4 кг в месяц = 25 месяцев).

# Расчёт остатка гречки:

# Каждый месяц тратится 4 кг. Остаток вычисляется по формуле:
# remaining = 100 - 4 * month.

# Вывод данных:

# Для каждого месяца выводится сообщение с текущим остатком гречки.