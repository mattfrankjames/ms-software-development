def main():
    fileName = input('what file? ')
    infile = open(fileName, 'r')
    
    total = 0.0
    count = 0
    line = infile.readline()
    while line != '':
        print(line)
        line = infile.readline()
        
main()