# Tuple example

def Tuple_add_multi(a,b):

    sum = a+b
    mul = a*b
    return(sum,mul)

x= input("enter first number")
y= input("Enter second number")

tup = Tuple_add_multi(x,y)

print("Sum of two number is " + str(tup[0]))
print("Multiplication of two number is " + str(tup[1]))
