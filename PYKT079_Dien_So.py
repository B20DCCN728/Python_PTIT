if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve = set(list(int(x) for x in input().split()))
        if len(solve) <= 1: print("0")
        else:
            convert_list = list(solve)
            print( - convert_list[0] + convert_list[len(convert_list) - 1] + 1 - len(solve))
        t -= 1
