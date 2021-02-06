def main():
    readFile = open(input('Enter sales file name: '), 'r')
    outFile = input('Enter the total sales file: ')
    outPutFile = open(outFile, 'w')
    strings = readFile.readlines()

    stringLists = []
    for string in strings:
        stringLists.append(string[1:].strip().split('$'))

    for stringList in stringLists:
        addOne = stringList[0].strip()
        addTwo = stringList[1].strip()
        sum = float(addOne) + float(addTwo)
        sumString = str(sum)
        print('${0} ${1} ${2}'.format(addOne.rjust(10), addTwo.rjust(
            10), sumString.rjust(10)), file=outPutFile)

    outPutFile.close()

    print('Done writing totals to {0} '.format(outFile))


main()
