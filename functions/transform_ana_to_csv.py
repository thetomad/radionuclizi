import pandas as pd

def transform(filename, year):

    file = open(filename,"r")
    
    f = file.read()

    fin = ''

    i = 0

    for letter in f:
        
        if letter == ' ' and not f[i-1] == ',':
            letter = ','
        elif letter == ' ':
            letter == ''
        else:
            pass

        i += 1

        fin = fin + letter

        fin = fin.replace(",,", ",")

    fin = ',Z,A,El,D,err \n' + fin
    
    filename = filename.rsplit('/',1)[-1]
    filename = filename.rsplit('.',1)[0]
    
    file2 = open(f"./databases/{year}/{filename}.csv", "w")
    file2.write(fin)

    file2.close()

    file2 = open(f"./databases/{year}/{filename}.csv", "r")

    lines = file2.readlines()

    file2.close()

    file2 = open(f"./databases/{year}/{filename}.csv", "w")
    
    for line in lines:
        line = line[1:-2] 

        file2.write(line + '\n')


    file2.close()
