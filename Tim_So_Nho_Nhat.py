from re import I


t = int(input())
while t > 0:
    arrMin = str(input())
    s = ""
    new_list = []
    for i in arrMin:
        if i >= '0' and i <= '9':
            s += i
        else: 
            if s != "": new_list.append(int(s))
            s = ""
    if s != "": new_list.append(int(s))
    new_list.sort()
    print(new_list[0])
    t -= 1