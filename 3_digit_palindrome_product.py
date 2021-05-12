def is_palindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10 # mod of num with 10 (returns last digit of number if num%10 == 0 return 0 )
        rev=rev*10+dig # add last digit to the reverse number
        num=num//10 # new num = num - last digit
    if(temp==rev):
        return True
    return False

if __name__ == "__main__":
    a = list(range(100,1000))
    b = list(range(100,1000))
    res = list(map(lambda x,y: str(x)+" "+str(y) if is_palindrome(x*y) else "-1" ,a,b))
    res = [x for x in res if x != '-1' ]
    print(res)