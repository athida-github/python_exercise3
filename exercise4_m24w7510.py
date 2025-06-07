f=open("paragraph.txt","r")
file = f.read()
words = file.split()
print("The file contains ",len(words),"words.")