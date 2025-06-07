open_file = input("Which file you want to copy: ")
copy_file = input("What is the new file name: ")
f_read=open(open_file,"r")
lines = f_read.readlines()
#print(lines)
#f_create=open("copy.txt","x")

f_write=open(copy_file,"w")
for line in lines:  
    f_write.writelines(line)
print("Content successfully copied to",copy_file)
f_write.close()
