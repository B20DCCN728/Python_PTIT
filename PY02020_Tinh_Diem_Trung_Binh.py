if __name__ == "__main__":
    n = int(input())
    solve = [float(x) for x in input().split()]
    solve.sort()
    Min = solve[0]
    Max = solve[n - 1]
    while Min in solve:
        solve.remove(Min)
    while Max in solve:
        solve.remove(Max)
    sum = 0
    for x in solve:
        sum += x
    print("%.2f" % (sum / len(solve)))
