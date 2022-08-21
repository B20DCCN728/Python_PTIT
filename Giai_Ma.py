
from queue import PriorityQueue


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        S = str(input())
        for i in range(1, len(S), 2):
            for x in range(0, int(S[i])):
                print(S[i - 1], end="")
        print()
        t -= 1