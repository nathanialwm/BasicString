#Count the words from an imported file
#Written by Nathanial Martin

f = input("Type a path to a text file: ")
file = open(f)
r = file.read().split()
c = len(r)
print(str(c) + " Words")
