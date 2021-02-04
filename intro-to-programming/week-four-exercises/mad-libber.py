def main():
    print('Madlib Maker')
    name = input('name: ')
    place = input('place: ')
    verb = input('verb: ')
    repeaterVerb = '{0} {0}'.format(verb[:len(verb)])
    print('One fine day {0} got up and went to {1}.'.format(name, place))
    print('When they got to {0} they decided to {1} for a little while.'.format(place, verb))
    print('After arriving at {0}, {1} was so excited, they screamed {2} at the top of their lungs.'.format(place, name, repeaterVerb))
    
main()
    