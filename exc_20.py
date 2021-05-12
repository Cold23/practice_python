import random
import math

def binary_search(seq,num):
    start = 0
    end = len(seq) - 1  
    while True :
        curr = math.floor((start + end)/2) 
        if start > end:
            return False
        if seq[curr] == num:
            return True
        elif seq[curr] > num:
            end = curr - 1
        elif seq[curr] < num:
            start = curr + 1



if __name__ == "__main__":
    seq =sorted([random.randint(0,10)for x in range(random.randint(2,100))])
    my_num = random.randint(0,10)
    print(binary_search(seq,my_num))