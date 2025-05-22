def int_palindrome(x):
    orignal = x
    rev = 0
    while x > 0:
        last_n = x%10
        print(f"Last Digit:",last_n)
        rev = rev * 10 + last_n
        print(f"Reverse Digit",rev)
        x = x // 10
    print(rev)
    if rev == orignal:  print("Palindrome")
    else:           print("Not a Palindrome")

num = int(input("Enter valid number to check it palindrome or not: "))
int_palindrome(num)
