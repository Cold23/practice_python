import re

if __name__ == "__main__":
    data = ''.join([line.rstrip() for line in open('exactly.txt')])
    print(''.join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))
    
