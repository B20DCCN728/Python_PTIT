if __name__ == "__main__":
    t = int(input())
    while t > 0:
        solve = [x for x in input().split(".")]
        if len(solve) != 4: print("NO")
        else:
            check = True
            for i in solve:
                try:
                    if int(i) > 255 or int(i) < 0:
                        print("NO")
                        check = False
                        break
                except:
                    check = False
                    print("NO")
                    break
            if check:    
                print("YES")
        t -= 1
