#Created by Campus
class file_input:
    def __init__(self) -> None:
        pass

    def open_file(name_file) -> list:
        data = []
        with open(name_file, 'r') as f:
            data = f.readlines()
        return data

if __name__ == "__main__":
    solve = file_input.open_file("DATA.in")
    res = []
    for i in solve:
        tmp = i.strip().split()
        for j in tmp:
            try:
                cnt = int(j)
                if cnt < -2147483648 or cnt > 2147483647:
                    res.append(j)
            except:
                res.append(j)
    res.sort()
    print(*res)