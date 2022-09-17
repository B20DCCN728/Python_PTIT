if __name__ == "__main__":
    t = int(input())
    while t > 0:
        S = str(input())
        if int(S) <= 10: print(int(S))
        else:
            n = len(S)
            new_list = []
            count = 1
            for i in range(0, n - 1):
                count *= 10
            for i in range(0, n):
                new_list.append(int(S[i]))
            for i in range(n - 2, -1, -1):
                if new_list[i + 1] >= 5:
                    new_list[i] += 1
            print(new_list[0] * count)
        t -= 1
