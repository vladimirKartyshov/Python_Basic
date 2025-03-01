# угадай число
# binary search

low = 1
high = 100

while low <= high:
    mid = (low + high) // 2
    print("Твое число равно, больше или меньше числа", mid, "?")
    answer = int(input("1 - равно, 2 - больше, 3 - меньше: "))
    if answer == 1:
        print("Мы угадали!")
        break
    elif answer == 2:
        # Число больше mid, ищем в верхней половине
        low = mid + 1
    elif answer == 3:
        # Число меньше mid, ищем в нижней половине
        high = mid - 1
    else:
        print("Пожалуйста, введите 1, 2 или 3.")

if low > high:
    print("Вы где-то соврали, такого числа нет!")
