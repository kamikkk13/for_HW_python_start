num = int(input())
count_1 = 0
count_2 = 0
for _ in range(num):
    money = int(input())
    if money == 1:
        count_1 += 1
    else:
        count_2 += 1
if count_1 > count_2:
    print(count_2)
else:
    print(count_1)