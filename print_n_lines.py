##PROGRAM TO PRINT N LINES FOLLOWING A PATTERN MATCH

def print_next_n_lines(infile,string,number):
    i = 0
    canprint = False
    with open(infile,'r') as f:
        for lines in f:
            if string in lines:
                canprint = True
                i = i + 1
            elif i >= 1 and i <= number :
                canprint = True
                i = i + 1
            else:
                continue
            if canprint:
                print(lines)
    f.close()
   
print_next_n_lines($FILE-NAME,"STRING",NUMBER-OF-LINES)
eg: print_next_n_lines(github.txt, "git", 10)

