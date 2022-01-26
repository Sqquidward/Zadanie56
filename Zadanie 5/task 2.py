count1 = int(input())
count2 = int(input())

elem_Angl = set()
elem_Nem = set()

for i in range(count1):
    elem_Angl.add(input())
for i in range(count2):
    elem_Nem.add(input())

digit = len(elem_Angl ^ elem_Nem)

if digit == 0:
    print("No")
else:
    print(digit)