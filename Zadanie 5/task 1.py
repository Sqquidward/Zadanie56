list = set()


for i in range(int(input())):
        list.add(input())

if input() in list:
    print("TRY ANOTHER")
else:
    print("OK")