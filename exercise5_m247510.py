search_keyword = input("Enter a word to search: programming: ")
f=open("paragraph.txt","r")
file_data = f.read()
words=file_data.split()
if search_keyword in [word.strip(".,!?;:@~#$").lower() for word in words]:
    print("The word ",search_keyword," was found.")
else:
    print("The word ",search_keyword," was not found.")    
f.close()
