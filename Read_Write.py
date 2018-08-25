default = "Omsakthi"

with open("intro.txt", 'r') as read_file:
    lines = read_file.readlines()
    print len(lines)
    

with open("write.txt", 'w') as write_file:   
     for line in lines:
       write_file.writelines("omsakthi" + line +'\n')
    

    
