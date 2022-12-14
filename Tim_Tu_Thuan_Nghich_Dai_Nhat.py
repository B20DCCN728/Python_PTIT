#Created by Campus
class file_input:
    def __init__(self) -> None:
        pass
    
    def open_file(name_file) -> dict:
        data = []
        with open(name_file, 'r') as f:
            data = f.readlines()
        return data

if __name__ == "__main__":
    solve = file_input.open_file("VANBAN.in")
    len_max = 0
    res = {}
    for i in solve:
        for tmp in i.strip().split():
            if tmp[::-1] == tmp:
                if len(tmp) > len_max:
                    res.clear()
                    len_max = len(tmp)
                    res[tmp] = 1
                else: 
                    if len(tmp) == len_max:
                        if tmp in res:
                            res[tmp] += 1
                        else: res[tmp] = 1
    for i in res:
        print(i, res[i])