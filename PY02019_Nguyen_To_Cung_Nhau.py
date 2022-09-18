import math
if __name__ == "__main__":
    n = int(input())
    input_list = [int(x) for x in input().split()]
    input_list.sort()
    for i in range(0, len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if math.gcd(input_list[i], input_list[j]) == 1: print(input_list[i], input_list[j])
    
