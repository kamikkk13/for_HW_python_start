# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# журавликов, чем Петя и Сережа вместе?

num = int(input("Введите количество журавликов: "))

Peter = num / 6
Serj = num / 6
Kate = 4 * Peter

if num % 2 == 0:

    print(
        f"Петя сделал {int(Peter)} шт, Сережа сделал {int(Serj)} шт , Катя сделала {int(Kate)} шт")
else:
    print("Число не может быть не четным")