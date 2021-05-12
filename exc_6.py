def isPalindrome(s):
    if s == s[::-1] :
        return True
    return False
    
if __name__ == "__main__":
    print(isPalindrome(input("Insert a word to check if it is palindrome: ")))