#Count Vowels
#written by Nathanial Martin

u = input("Type anything you'd like: ")
arr = ['a', 'e', 'i', 'o', 'u',]
v = 0

for x in range(0, len(arr)):
    c = u.count(arr[x])
    print(arr[x] + ": " + str(c))
    v += u.count(arr[x])

print("Total Vowels: " + str(v))

    

    
