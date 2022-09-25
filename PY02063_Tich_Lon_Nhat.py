if __name__ == "__main__":
    n = int(input())
    data = [int(x) for x in input().split()]
    data.sort()
    res = []
    res.append(data[0] * data[1])
    res.append(data[0] * data[1] * data[n - 1])
    res.append(data[n - 1] * data[n - 2])
    res.append(data[n - 1] * data[n - 2] * data[n - 3])
    print(max(res))
