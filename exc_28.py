def max_of(seq):
    m = seq[0]
    for i in seq[1:len(seq)]:
        if i > m:
            m = i 
    return m

if __name__ == "__main__":
    print(max_of([1,2,3,4,5,6,7,8,20,8]))