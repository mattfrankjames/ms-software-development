def main():

    listToCheck = []
    numberInput = ''
    
    while numberInput != -1:
        if len(listToCheck) == 0:
            numberInput = int(input('Enter the first number: '))
        else:
            numberInput = int(input('Next: '))
        if numberInput != -1:
            listToCheck.append(numberInput)
            
    if(len(set(listToCheck)) == len(listToCheck)):
       print('The sequence {} is unique!'.format(listToCheck))
    else:
       print('The sequence {} is NOT unique!'.format(listToCheck))
main()