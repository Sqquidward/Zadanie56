#Если ученики идут по порядку

count1 = int(input())
count2 = int(input())
count3 = int(input())

elem_Angl = set()
elem_Nem = set()
elem_Fran = set()

for i in range(count1):
    elem_Angl.add(input())
for i in range(count2):
    elem_Nem.add(input())
for i in range(count3):
    elem_Fran.add(input())

answer = len((elem_Angl | elem_Fran | elem_Nem) ^ (elem_Angl ^ elem_Nem ^ elem_Fran))
if answer == 0:
    print("No")
else:
    print(answer)

print(elem_Angl ^ elem_Nem ^ elem_Fran)