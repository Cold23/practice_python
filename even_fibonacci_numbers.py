def fibbo(limit):
    seq = [1,1]
    a,b=1,1
    while b< limit:
        a,b = b , a+b
        seq.append(b)
    return seq

if __name__ == "__main__":
    res = sum([x for x in fibbo(4000000) if x % 2 ==0])
    print(res)
    