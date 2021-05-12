import math

def amicable_sum(limit):
    amicables = set()

    for num in range(2,limit+1):
        if num in amicables:
            continue
        sum_of_facts = sum([fact for fact in range(1,math.floor(num/2)+1) if num % fact == 0 ]) # sum of factors for num
        sum_of_facts2 = sum([fact for fact in range(1,math.floor(sum_of_facts/2)+1) if sum_of_facts% fact == 0 ]) # sum of factors for sum of factors of num
        if num == sum_of_facts2 and num != sum_of_facts: # if num == sum of factors of the sum of factors of num and not equal to its own sum of factors then num and sum_of_facts2 are amicable
            amicables.add(num)
            amicables.add(sum_of_facts2)
    return amicables

if __name__ == "__main__":
    print(sum(amicable_sum(10000)))