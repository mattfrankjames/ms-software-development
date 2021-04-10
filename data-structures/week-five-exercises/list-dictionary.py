from random import randrange


def main():
    verbs = ['run', 'swim', 'spit', 'kick', 'dive', 'ride', 'jog']

    nouns = {
        0: 'Steve',
        1: 'Matt',
        2: 'Willy',
        3: 'Matilda',
        4: 'basketball',
        5: 'cheese',
        6: 'pig',
    }

    def mad_libs(nouns, verbs):
        return 'There once was a {0} who liked to {1}. Every now and then, they would {2} on {3}. After a while, this became untenable, so {4} decided to {5} and retire to a nice, quiet {6}.'.format(nouns[randrange(0, 6)], verbs[randrange(0, 6)], verbs[randrange(0, 6)], nouns[randrange(0, 6)], nouns[randrange(0, 6)], verbs[randrange(0, 6)], nouns[randrange(0, 6)])
    print(mad_libs(nouns, verbs))

    print(hash(verbs[2]))


main()
