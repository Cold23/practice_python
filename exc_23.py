def read_file(filename):
    with open(filename,'r') as open_file:
        return open_file.read().rstrip()

if __name__ == "__main__":
    file1 = read_file("primenumbers.txt")
    file2 = read_file("happynumbers.txt")
    res = []
    numbs1 = file1.split("\n")
    numbs2 = file2.split("\n")
    for x in numbs1:
        if x in numbs2 :
            res.append(x)
    print(res)