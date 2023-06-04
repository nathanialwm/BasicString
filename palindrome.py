#Check if string is palindrome
#Palindrome is a word or phrase that reads the same backwords and normally
#Written by Nathanial Martin

u = input("Type anything you'd like: ")
c = u[::-1]

if c.lower() == u.lower():
    print("Yes! That is a palindrome!")
else:
    print("Sorry " + u + " is not a palindrome!")
