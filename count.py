def Check(num):
    count = 0   
    with open("number.txt","r") as f:
        array = []
        for line in f:
            array.extend(line.split(','))
            array = [arr.strip() for arr in array]
        #print(len(array))

        print(array)
       # print(num)
        
        for item in array:   
            if (int(item) == int(num)):
                count = count + 1       

        print("Count for {num} is :" + str(count))
        

num = int(input("Enter the number to search"))
Check(num)

