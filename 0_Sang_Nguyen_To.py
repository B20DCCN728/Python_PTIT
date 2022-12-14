#Sang Nguyen To Pro Max
era = [0] * 1000001
def era_pro_max():
    era[0] = era[1] = 1
    for i in range(2, 1000):
        if era[i] == 0:
            for j in range(i * i, 1000001, i):
                era[j] = 1
