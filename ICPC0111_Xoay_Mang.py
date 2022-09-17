if __name__ == "__main__":
    n = int(input())
    while(n > 0):
        t, d = [int(x) for x in input().split()]
        list_arr = [int(x) for x in input().split()]
        for i in range(d, t): print(list_arr[i], end=" ")
        for i in range(0, d): print(list_arr[i], end=" ")
        print()
        n -= 1
