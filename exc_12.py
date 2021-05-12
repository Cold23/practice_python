def firstLast(x):
    res = x[0:len(x):len(x)-1]
    return res

if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8,9]
    print(firstLast(x))