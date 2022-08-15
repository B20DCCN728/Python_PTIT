number = int(input())
num_1 = 0
num_2 = 0
while number > 0:
    if number % 10 == 4: num_1 += 1
    elif number % 10 == 7: num_2 += 1
    number //= 10
res = num_1 + num_2
if res == 4 or res == 7:
    print("YES")
else: print("NO")
