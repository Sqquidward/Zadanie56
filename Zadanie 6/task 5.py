text = input()
sim = text[0]
text = text[1::]
print(text)


x: int = 0
y: int = 0
pustota = ""
print(sim, end="")
for i in range(len(text)):
    if text[i] == ">":
        print(end="")
        print(sim)
        x += 1
    elif text[i] == "<":
        x -= 1
    elif text[i] == "V":
        for j in range(x-2):
            pustota += " "
        print(pustota, sim)