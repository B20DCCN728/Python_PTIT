#Created by Campus

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        p, k = [], 0
        solve = input()
        for i in range(len(solve)):
            if solve[i] == '(':
                k += 1
                p.append(k)
                print(k, end= " ")
            elif solve[i] == ')':
                print(p.pop(), end= " ")
            else: pass
        print()
        
                

