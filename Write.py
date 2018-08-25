
with open("write.txt", 'w') as write_file:
    write_file.write(" hello this is my first sentence to write")

with open("write.txt", 'a') as write_file:   
    write_file.write("\n hello this is my second sentence to write")
    write_file.write("\n hello this is my third sentence to write")
    write_file.write("\n hello this is my forth sentence to write")

quotes = [

"\n Today I bake and tomorrow I brew"
"\n Jesus come and save the world we need a teacher"
"\n Amma please help me"

]
    
with open("write.txt", 'a') as write_file:
    write_file.writelines(quotes)
    
