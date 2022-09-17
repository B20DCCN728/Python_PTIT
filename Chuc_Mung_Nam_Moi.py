if __name__ == "__main__":
    n = int(input())
    list = []
    while n > 0:
        s = input()
        if s not in list: list.append(s)
        n -= 1
    print(len(list))