if __name__ == "__main__":
    limit = 1000
    for a in range(1,limit+1):
        for b in range(a+1,limit+1):
            c = limit-a-b
            if a*a + b*b == c*c:
                print(list([a,b,c]))