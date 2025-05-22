
def ispalindrom(x):
    x= x.lower()
    rev = ""
    for i in range(len(x) -1, -1, -1):
         rev += x[i]
    if rev == x: 
         print("Palindrome")
    else:
         print("Not a Palindrome")
    
x = input("Enter string to check weather it is palindrome or not: ")
ispalindrom(x)


    