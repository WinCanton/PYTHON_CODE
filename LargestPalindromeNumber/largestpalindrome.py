palinlist = []
for i in range(100, 999, 1):
    for j in range(100, 999, 1):
        x = str(i * j)
        if x == x [::-1]:
            palinlist.append(int(x))
        else:
            pass

print max(palinlist)