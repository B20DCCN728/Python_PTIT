if __name__ == "__main__":
    n = int(input())
    data = []
    while True:
        a = [int(x) for x in input().split()]
        data.extend(a)
        if len(data) == n: break

    even = []
    odd = []
    location = []
    for i in range(len(data)):
        if data[i] % 2 == 0: 
            even.append(data[i])
            location.append(i)
        else: odd.append(data[i])
    even.sort(reverse = True)
    odd.sort()
    res = []
    for i in range(n):
        if i in location:
            print(even[-1], end = " ")
            even.pop()
        else: 
            print(odd[-1], end = " ")
            odd.pop()