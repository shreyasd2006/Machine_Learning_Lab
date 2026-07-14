list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

count = 0

for x in set(list1):
    if x in list2:
        count += 1

print("Common elements:", count)