list = []
word_1 = input()
list.append(word_1)
while True:
    word_2 = input()
    list.append(word_2)
    if list[len(list)-2][-1] != list[len(list)-1][0]:
        print(list[len(list)-1])
