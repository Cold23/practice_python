import sys

def collatz_sequence(n):
    seq = []
    seq.append(n)
    while n > 1 :
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        seq.append(n)
    return len(seq)

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    ans = max(range(1,1000001),key=collatz_sequence)
    print(ans)
