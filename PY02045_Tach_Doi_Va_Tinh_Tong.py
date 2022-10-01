if __name__ == "__main__":
    n = input()
    while len(n) > 1:
        x = int(n[0:int(len(n) / 2)]) + int(n[int(len(n) / 2):])
        print(x)
        n = str(x)
