if __name__ == "__main__":
    n = int(input())
    new_list = [int(x) for x in input().split()]
    solve = []
    for i in new_list:
        if len(solve) == 0:
            solve += [i]
        else:
            if (solve[-1] + i) % 2 == 0:
                solve.pop()
            else:
                solve += [i]
    print(len(solve))
