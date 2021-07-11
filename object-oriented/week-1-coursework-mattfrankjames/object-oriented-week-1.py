class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, item):
        return item.upper() in (i.upper() for i in self.__myTeam)
        
    def __iter__(self):
        return iter(self.__myTeam)
    def __str__(self):
        return '\n'.join(self.__myTeam)
    
def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    
    print('Number of classmates:')
    print (len(classmates))
    print()
    
    # Returns True as 'Tim' is in classmates
    print('Is Tim in the class?')
    print('Tim' in classmates)
    print()
    
    # Returns False as 'Sam' is not in classmates
    print('Is Sam in the class?')
    print('Sam' in classmates)
    print()
    
    # Use the iterator
    print('List of teammates in the class using iterator:')
    for i in classmates:
        print(i)
    print()
    
    # Use the string method
    print('List of teammates in the class using str method:')
    print(classmates)

main()