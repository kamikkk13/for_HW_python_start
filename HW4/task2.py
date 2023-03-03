import random

list = [random.randint(1, 10) for _ in range(int(input()))]

# print(list)
# list_sum = [sum([list[i -1], list[i], list[i + 1]]) if i != len(list) - 1 else sum([list[i - 1], list[i], list[0]]) for i in range(len(list))]
# print(list_sum)
# list_max = max([sum([list[i -1], list[i], list[i + 1]]) if i != len(list) - 1 else sum([list[i - 1], list[i], list[0]]) for i in range(len(list))])

print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль: {max([sum([list[i -1], list[i], list[i + 1]]) if i != len(list) - 1 else sum([list[i - 1], list[i], list[0]]) for i in range(len(list))])}')