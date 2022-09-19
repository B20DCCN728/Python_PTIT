def Solution(solve):
    solve = solve.replace("688", "")
    if(len(solve) == 0): 
        print("YES")
        return
    solve = solve.replace("68", "")
    if(len(solve) == 0): 
        print("YES")
        return
    solve = solve.replace("6", "")
    if(len(solve) == 0):
        print("YES")
        return 
    print("NO")
    return

if __name__ == "__main__":
    solve = input()
    Solution(solve)
    
    
