f_read = open("log.txt","r")
file = f_read.read()
lines = file.splitlines()
counter = 1
for line in lines:
    if "ERROR" in line:
        counter += 1
        print(line.strip()) 
print("Total errors: ",counter)