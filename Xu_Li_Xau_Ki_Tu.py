if __name__ == "__main__":
    a = set(list(x for x in input().lower().split()))
    b = set(list(x for x in input().lower().split()))
    union = list(a.union(b))
    union.sort()
    inter = list(a.intersection(b))
    inter.sort()
    print(" ".join(union))
    print(" ".join(inter))