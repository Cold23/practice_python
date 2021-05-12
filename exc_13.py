def fibbonaci_sequence(howLong):
    if howLong==1:
        b=[1]
    elif howLong!=1:
        b=[1,1]
    for _ in b:
        if len(b)<howLong: 
            i = b[-1]+b[-2]
            b.append(i)
        else:
            break
    print(b)

if __name__ == "__main__":
    howLong=int(input('Please input number: '))
    fibbonaci_sequence(howLong)
    