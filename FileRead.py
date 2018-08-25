first_file = open("intro.txt")

#for line in first_file:
    #print(line.rstrip())

#first_file.seek(0)

#lines = first_file.readlines()
#print(lines)

first_file.seek(50)
file_text = first_file.read(100)
print(file_text)


first_file.close()


