# Задача Почта
hour = int(input("Во сколько приходите?"))
if (
    (hour >= 8 and hour < 10)
    or (hour >= 12 and hour < 14)
    or (hour >= 15 and hour < 18)
    or (hour >= 20 and hour < 22)
):
    print("Можно получить посылку")
else:
    print("Нельзя получить посылку")
