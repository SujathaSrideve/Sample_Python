def Figure(n):
    
    for i in range(1,n+1):
        #print("\n")
        s=''
        for j in range(0,i):
            s+='*'
        print(s)
            
x = input("Enter the number to form a figure")
Figure(x)
