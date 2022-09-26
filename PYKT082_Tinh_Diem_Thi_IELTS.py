#CampusETH
class IELTS:
    def __init__(self) -> None:
        pass
    def convertScore(n) -> float:
        if n >= 39 and n <= 40: return 9.0
        elif n >= 37 and n <= 38: return 8.5
        elif n >= 35 and n <= 36: return 8.0
        elif n >= 33 and n <= 34: return 7.5
        elif n >= 30 and n <= 32: return 7.0
        elif n >= 27 and n <= 29: return 6.5
        elif n >= 23 and n <= 26: return 6.0
        elif n >= 20 and n <= 22: return 5.5
        elif n >= 16 and n <= 19: return 5.0
        elif n >= 13 and n <= 15: return 4.5
        elif n >= 10 and n <= 12: return 4.0
        elif n >= 7 and n <= 9: return 3.5
        elif n >= 5 and n <= 6: return 3.0
        else: return 2.5 

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = [float(x) for x in input().split()]
        solve[0] = IELTS.convertScore(solve[0])
        solve[1] = IELTS.convertScore(solve[1])
        score = (solve[0] + solve[1] + solve[2] + solve[3]) / 4
        if score - int(score) >= 0.75: print("{:.1f}".format(int(score) + 1))
        elif score - int(score) >= 0.25: print("{:.1f}".format(int(score) + 0.5))
        else: print('{:.1f}'.format(int(score)))
        t -= 1
        
