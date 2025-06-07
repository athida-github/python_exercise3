
f_read = open("grades.txt","r")
lines = f_read.readlines()
counter=0
total_grade=0
for line in lines:
    value = line.strip().split(", ")
    grade=int(value[1].replace("Grade: ",""))
    total_grade += grade
    counter+=1
print("Average Grade:", total_grade/counter)


    