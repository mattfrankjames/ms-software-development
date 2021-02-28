from random import randrange

# get target sum

def getTargetSum():
    targetSum = int(input('Enter the target sum to roll for: '))
    return targetSum

# get the two dice roll values

def getRollValues(numRolls):
    rolls = []
    for roll in range(numRolls):
        rolls.append(randrange(1, 7))
    rollOne, rollTwo = rolls[0:numRolls]
    sum = rollOne + rollTwo
    return rollOne, rollTwo, sum


def printSumMessage(rollOne, rollTwo, sum):
    print('Roll: {0} and {1}, sum is {2}'.format(rollOne, rollTwo, sum))

def main():
    targetSum = getTargetSum()
    rollOne, rollTwo, sum = getRollValues(2)
    rollCount = 0
    while targetSum != sum:
        printSumMessage(rollOne, rollTwo, sum)
        rollOne, rollTwo, sum = getRollValues(2)
        sum  = rollOne + rollTwo
        rollCount = rollCount + 1
    printSumMessage(rollOne, rollTwo, sum)
    print('Got it in {} tries!'.format(rollCount))
        
    
    
main()