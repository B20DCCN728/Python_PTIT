from distutils.command.install_scripts import install_scripts


if __name__ == "__main__":
    res = [0] * 42
    count = 0
    while True:
        base = [int(x) for x in input().split()]
        count += len(base)
        for x in base:
            res[x % 42] = 1
        if count == 10: break
    asw = 0
    for x in range(42):
        if res[x] > 0: asw += 1
    print(asw)