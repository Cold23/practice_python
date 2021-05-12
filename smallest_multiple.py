import math 
# most optimal solution
def compute():
    ans = 1
    for i in range(1, 21):
        ans = ans *(i // math.gcd(i, ans)) # elaxisto koino pollaplasio tou x me to y einai  ans = x * y/gcd(x,y) kai tou ans me to 2  ans = ans * 2/gcd(ans,2) meta ans me to 3 ans = ans * 3/gcd(ans,3)  
    return ans

if __name__ == "__main__":
    # is_product = False
    # x = 20
    # i = range(1,21)
    # while not is_product:
    #     x += 20
    #     res = [y for y in i if x % y == 0]
    #     if len(res) == 20 :
    #         is_product = True
    # print(x) my first try
    print(compute())