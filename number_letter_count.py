one_digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def letter_to_word(num):
    num_str = str(num)
    if len(num_str) == 1:
        return(one_digit[num])
    elif len(num_str) == 2:
        return two_digit_to_string(num)
    elif len(num_str) == 3:
        ans = one_digit[int(num_str[0])]+"hundred"+"and"+two_digit_to_string(int(num_str[1:]))
        return ans
    return "onethousand"

def two_digit_to_string(num):
    num_str = str(num)
    if num < 20 :
        return one_digit[num]
    else:
        ans = tens[int(num_str[0])]
        if int(num_str[1]) != 0:
            ans +=one_digit[int(num_str[1])]
        return ans

if __name__ == "__main__":
    ans = sum([len(letter_to_word(i)) for i in range(1,1001)])
    print(ans)

