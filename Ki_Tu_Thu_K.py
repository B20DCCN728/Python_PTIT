data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Character:
    def __init__(self) -> None:
        pass

    def change(n, k):
        res = ""
        for i in range(n):
            res = res + data[i] + res
        return res[k - 1]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, k = [int(x) for x in input().split()]
        print(Character.change(n, k))
        t -= 1