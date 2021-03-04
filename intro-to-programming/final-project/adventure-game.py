# Potential outcomes
# 1. Make it to the goal
# 2. Get killed by one of the enemies
# 3. Earn an extra life
# 4. Maybe provide the option to go again

# Potential areas to earn extra credit
# 1. Use graphics!
# 2. More than one scenario
# 3. Maybe store characters in a JSON file and parse it
# 4. Character can gain some info as an outcome to a step and not just get attacked or collect something.
# 5. Maybe the character could encounter quicksand and have to start over


class Character:
    def __init__(self, name):
        self.name = name
        self.trinkets = []
        self.resources = []
    def attack():
        # TODO: add an attack method here
        # Use random()
        print('attack')
    def collect():
        # TODO: add trinket to trinkets list
        #Use random()
        print('get a trinket')
    def move(self):
        # TODO: Make the character move
        # Use random()
        print('move')
def printWelcomeMessage():
    print('Welcome to Hogwarts, Harry! You need to find the Sorceror\'s Stone in ten steps!')
    
def makeProgress(character):
    proceed = input('Only ten weeks to find the stone! Want to proceed? (y/n) ')
    if proceed == 'y':
        character.move()
        print(character)
    
def main():
    printWelcomeMessage()
    Harry = Character('Harry')
    makeProgress(Harry)
    #dictonary of the trinket chest
    treasureChest = {}
    
    # Character.Move()
    
    #Collect a trinket
    
    # Character.collect()
    
    # printWarningMessage()
    
    #instantiate new character enemy
    
    # generateEnemy()
    # Enemy attacks
    # Character.attack()
    
    # printGameResult()

main()
        