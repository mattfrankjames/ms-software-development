# acculator variable
baseScore = 0
# How many days to score
daysToScore = int(input('How many days of scores? '))

# need to loop over the number of days scored

for n in range(1, daysToScore + 1):
    baseScore = baseScore + int(input('Enter the score for day ' + str(n) + ': '))
    
print('The total score for ' + str(daysToScore) + ' days is ' + str(baseScore))
