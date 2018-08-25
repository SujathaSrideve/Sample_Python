
def seq_filter(line):
    return '>' not in line


with open("intro.txt") as sec_files:
 lines = sec_files.readlines()

print(list(filter(seq_filter,lines)))

