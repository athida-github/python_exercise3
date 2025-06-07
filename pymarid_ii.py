def print_pyramid(n):
    for i in range(1,n + 1):
        #space to print
        for j in range(n - i):
            print(" ",end="")
        #star to print     
        for k in range(1, 1*i):                                
            print("*",end="")               
            
        print()

if __name__ == "__main__":
   print_pyramid(7)