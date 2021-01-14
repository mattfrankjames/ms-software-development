chorus = 'Go, team, go!\nDefeat your foe.'
verse = 'Simply the best,\nBetter than the rest.'

def basicChant(lyric):
    print(lyric)
    
def extraChant(lyricA, lyricB):
    print(lyricA, lyricB)
    print(lyricA)
    print('\n')

def sing_fight_song():
    basicChant(chorus)
    print('\n')
    extraChant(chorus, verse)
    extraChant(chorus, verse)
    basicChant(chorus)
    
sing_fight_song()
