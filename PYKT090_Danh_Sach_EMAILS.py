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
    solve = file_input.open_file("CONTACT.in")
    res = []
    for i in solve:
        tmp = i.strip().lower()
        if tmp not in res:
            res.append(tmp)
    res.sort()
    for i in res: print(i)
