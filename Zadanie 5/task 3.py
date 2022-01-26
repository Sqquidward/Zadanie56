#Если ученики идут в произвольном порядке

count1 = int(input())
count2 = int(input())
count3 = int(input())

list = []
variety = set()

N = count1+count2+count3
for i in range(N):
    list.append(input())

for elem in list:
    variety.add(elem)

answer = 0
for m in variety:
    count = 0
    for i in range(len(list)):
        if m == list[i]:
            count +=1
    if count == 2:
        answer+=1

print(answer)