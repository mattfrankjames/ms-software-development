def main():
    print('Welcome to the Colf Club Helper!')
    print('Tell me your situation, and I\'ll recommend a club.')
    
    greenBool = input('Did you hit it on the green (y/n)? '.lower())
    
    length = int(input('How far is the ball from the hole? '))
    
    clubRec = ''
    
    if greenBool.lower() == 'y':
        clubRec = 'Putter'
    elif length >= 200:
        clubRec = 'Driver'
    elif length < 200 and length > 140:
        clubRec = '5-Iron'
    elif length <= 140 and length > 100:
        clubRec = '9-Iron'
    else:
        clubRec = 'Pitching Wedge'
    print('I recommend using your {0} '.format(clubRec))
    

main()