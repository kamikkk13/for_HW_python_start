import random

list_1 = [random.randint(1, 20) for _ in range(int(input()))]
list_2 = [random.randint(1, 20) for _ in range(int(input()))]
my_list = list(set(list_1) & set(list_2))
if my_list != []:
    my_list.sort()
    print(*my_list)
else:
    print("No common numbers")
