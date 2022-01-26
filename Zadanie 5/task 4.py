count1 = int(input())
count2 = int(input())

list1 = set()
list2 = []

for i in range(count1):
    list1.add(input())
for i in range(count2):
    list2.append(input())

for elem in list2:
    if elem in list1:
        print("Yes")

    else:
        print("No")