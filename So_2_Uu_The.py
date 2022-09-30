#Created by Campus
a = [0, 1, 2]
data = []
#
def check(solve) -> bool:
    count = 0
    for i in solve: 
        if i == "2": count += 1
    if count > len(solve) / 2: return True
    else: return False
#
def Try(s):
    if check(s): data.append(s)
    if len(s) < 6:
        for i in a:
            Try(s + str(i))
#
if __name__ == "__main__":
    Try("1")
    Try("2")
    data = sorted([int(x) for x in data])
    t = int(input())
    while t > 0:
        n = int(input())
        for i in range(n): print(data[i], end = " ")
        print()
        t -= 1