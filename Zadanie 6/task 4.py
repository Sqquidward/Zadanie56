text = input()
count = int(input())

for i in range(len(text)):
    if ord(text[i])>1105 or ord(text[i])<1040:
        print(chr(ord(text[i])), end="")
    else:
        print(chr(ord(text[i])+count), end="")