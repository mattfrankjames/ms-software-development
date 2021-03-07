from random import *

class Character:
    def __init__(self, name):
        self.name = name
        self.horcruxes = []
        self.lifePoints = 100
    def attack(self, enemy):
        damage = randrange(1, 10)
        enemy.lifePoints = enemy.lifePoints - damage
    def collect(self, horcrux):
        # Check to see if we already have the horcrux and collect it if we don't
        if horcrux not in self.horcruxes:
            print('You found a Horcrux! Put {0} in your chest!'.format(horcrux))
            self.horcruxes.append(horcrux)
        else:
            print('Uh oh, looks like a fake {0}'.format(horcrux))
    def move(self):
        print('move')
        
class Enemy:
    def __init__(self, name):
        self.name = name
        self.lifePoints = 10
    def attack(self, character):
        damage = randrange(1, 10)
        character.lifePoints = character.lifePoints - damage
        
def printWelcomeMessage():
    character = input('Welcome to The Harry Potter Adventure game! Which character would you like to be?')
    print('Welcome to Hogwarts, {0}! You need to find the all the horcruxes in ten weeks!'.format(character))
    return character
              
def makeProgress(character, weeks):
    proceed = input('Only {0} weeks to find the horcruxes! Want to proceed? (y/n) '.format(weeks))
    if proceed == 'y':
        character.move()
    else:
        confirm = input('Giving up so soon? Keep going! (y/n)')
        if(confirm == 'n'):
            print('Ok, try again soon!')
            exit()

def actionToTake():
    actionToTake = ''
    if(random() < .5):
        actionToTake = 'advance'
    else:
        actionToTake = 'defend'
    return actionToTake

    
def encounterEnemy(character, enemy, action):  
    print('Oh no, it\'s {0}, they want to {1}!'.format(enemy, action))
    enemy = Enemy(enemy)
    while(enemy.lifePoints >= 0 and character.lifePoints >= 0):
        print('{0} is attacking you!'.format(enemy.name))
        enemy.attack(character)
        fightBack = input('Do you want to fight back? (y/n)')
            
        if(fightBack == 'y'):
            character.attack(enemy)
            print('{0} is attacking you!'.format(enemy.name))
            enemy.attack(character)
            fightBack = input('Do you want to fight back? (y/n)')
                
        elif(fightBack == 'n'):
            print('{0} has defeated you! Better luck next time! You have {1} horcruxes and {2} life points'.format(enemy.name, len(character.horcruxes), character.lifePoints))
            exit()
    if(character.lifePoints <= 0):
        print('{0} has defeated you! Better luck next time! You have {1} horcruxes and {2} life points'.format(enemy.name, len(character.horcruxes), character.lifePoints))
        exit()
    elif(enemy.lifePoints <=0):
        print('You have defeated {0}!'.format(enemy.name))

def printOutcome(character, limit):
    if(len(character.horcruxes) == 6):
        print('Congratulations! You found all {0} horcruxes and have {1} life points left!'.format(len(character.horcruxes), character.lifePoints))
    if(limit == 0):
        print('Term is over and you only found {0} horcruxes. At least you have {1} life points left. Better luck next time!'.format(len(character.horcruxes), character.lifePoints))
    
            
enemies = {
    0: 'Voldemort',
    1: 'Bellatrix Lestrange',
    2: 'Lucius Malfoy',
    3: 'Wormtail',
    4: 'Barty Crouch Jr.',
    5: 'Fenrir Grayback',
    6: 'Igor Karkaroff',
    7: 'Corban Yaxley'
}
spells = {
    0: 'cast the Imperius Curse',
    1: 'cast the Cruciatus Curse',
    2: 'cast Avada Kedvara'
}
horcruxes = {
    0: 'Riddle\'s Diary',
    1: 'Marvolo Gaunt\'s ring',
    2: 'Helga Hufflepuff\'s cup',
    3: 'Slytherin\'s locket',
    4: 'Ravenclaw\'s diadem',
    5: 'Nagini',
}
    
def main():
    weeksRemaining = 10
    
    hero = printWelcomeMessage()
    
    randomHorcrux = randrange(0, 6)
    randomSpell = randrange(0, 3)
    randomEnemy = randrange(0, 8)
    
    wizard = Character(hero)
    
    while(weeksRemaining != 0 and wizard.lifePoints > 0 and len(wizard.horcruxes) < 6):
        makeProgress(wizard, weeksRemaining)
        move = actionToTake()
        
        weeksRemaining = weeksRemaining - 1
        randomHorcrux = randrange(0, 6)
        randomSpell = randrange(0, 3)
        randomEnemy = randrange(0, 8)
        if(move == 'advance'):
            wizard.collect(horcruxes[randomHorcrux])
        elif(move == 'defend'):
            encounterEnemy(wizard, enemies[randomEnemy], spells[randomSpell])
    
    printOutcome(wizard, weeksRemaining)
 
main()
        