if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = str(input())
        money, ir, target = s.split()
        money = float(money)
        ir = float(ir)
        target = float(target)
        for i in range(1, 100000):
            money *= (ir * 0.01) + 1
            if money >= target: 
                print(i)
                break
        t -= 1