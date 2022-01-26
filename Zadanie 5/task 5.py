count = int(input())

list = []

for i in range(count):
    list.append(input())

answer = 0

for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        if list[i]==list[j]:
            answer +=1
            break
print(answer)

# Иванов
# Петров
# Сидоров
# Петров
# Иванов
# Петров