from operator import le
def solve(S):
    count = 1
    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            print(f"{count}{S[i - 1]}", end="")
            count = 1
    print(f"{count}{S[len(S) - 1]}", end="")

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        S = str(input())
        solve(S)
        print()
        t -= 1