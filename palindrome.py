def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reverse = 0
    original = x
    
    while x > 0:
        reverse = reverse * 10 + x % 10
        x //= 10
        
    return reverse == original

num = int(input("Enter an integer: "))

if isPalindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
