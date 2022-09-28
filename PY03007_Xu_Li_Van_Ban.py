from re import *
if __name__ == "__main__":
    solve = ""
    regex = "[\w\s:,]+"
    while True:
        try:
            x = input()
            solve += x + ""
        except EOFError: break
    solve = findall(regex, solve)
    for i in solve:
        j = i.lower().split()
        j[0] = j[0].title()
        print(" ".join(j))
