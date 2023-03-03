n = int(input("Input amount numbers in array: "))
list = [int(input()) for _ in range(n)]
number = int(input("Number: "))
print(f"How many times we see a number {number} in the array: {list.count(number)}")