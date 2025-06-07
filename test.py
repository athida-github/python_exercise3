import os

pth = os.getcwd()
file_path=os.path.join(pth, 'example.txt')
print(f"Current working directory: {pth}")  
print(file_path)

with open(file_path,"r") as file:
    content=file.read()
    print(content)
    print("======== input file read ==========\n\n")
    
    words = content.split()
    print(words)
    
    print("Number of words",len(words))
    lines=content.splitlines()
    print(lines)
    print("No. of line : ",len(lines))
    print(len(content))
    wordss = [word.strip(".,!?;:@").lower() for line in lines for word in line.split()] 
    print(wordss)


