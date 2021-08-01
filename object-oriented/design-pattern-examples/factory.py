from abc import ABC, abstractmethod
from datetime import date

# -- CLASS DEFINITIONS  -----------------------------------------------------

class BlogContributor(ABC):

    # Static Variables (Class-Level)

    __numberOfContributors = 0

    # Constructor - called when object is created
    
    def __init__(self, contributorID, firstName, lastName, contributorType):
        self.__contributorID = contributorID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__contributorType = contributorType
        self.__hireDate = date.today()
        self.__permissions = []
        BlogContributor.__numberOfContributors += 1
 
    # Destructor - called when object is deleted
 
    def __del__(self):
        print("University employee {} has been deleted.\n".format(self.__contributorID))
        BlogContributor.__numberOfContributors -= 1
 
    # Public Methods - accessible from outside instantiated object
    def updatePermissions(self, permissions=[]):
        self.__permissions.insert(permissions)
    
    def setContributorSince(self, contributeStartYear, contributeStartMonth, contributeStartDay):
        self.__contributeStartDate = date(contributeStartYear, contributeStartMonth, contributeStartDay)

    def showContributorInformation(self):
        print("Contributor ID: ", self.__contributorID)
        print("Contributor Name: ", self.__firstName + " " + self.__lastName)
        print("Hire Date: ", self.__contributorStartDate)

    def getContributorName(self):
        return self.__firstName + " " + self.__lastName
    
    def getPermissions(self):
        permissions = []
        for permission in self.__permissions:
            permissions.insert[permission]
        return permissions

    @abstractmethod
    def showContributorDetails(self):
        raise NotImplementedError

    @staticmethod # Class-level method, not object-level method
    def showNumberOfContributors():
        print("Number of Blog Contributors = ", BlogContributor.__numberOfContributors)

class BlogAuthor(BlogContributor):
    
    # Static constants

    __CONTRIBUTOR_TYPE = "Author"
    
    # Constructor
    
    def __init__(self, contributorID, firstName, lastName):
        BlogContributor.__init__(self, contributorID, firstName, lastName, BlogAuthor.__CONTRIBUTOR_TYPE)
        self.__permissions = ['create', 'update', 'delete']
        
    # public methods
    def showContributorDetails(self):
        BlogContributor.showContributorInformation(self)
        print("permissions:", BlogContributor.getPermissions(self))
    
class BlogEditor(BlogContributor):
    
    # Static constants

    __CONTRIBUTOR_TYPE = "Editor"
    
    # Constructor
    
    def __init__(self, contributorID, firstName, lastName):
        BlogContributor.__init__(self, contributorID, firstName, lastName, BlogEditor.__CONTRIBUTOR_TYPE)
        self.__permissions = ['update', 'publish']
     # public methods
    def showContributorDetails(self):
        BlogContributor.showContributorInformation(self)
        print("permissions:", BlogContributor.getPermissions(self))

class BlogAdmin(BlogContributor):
    
    # Static constants

    __CONTRIBUTOR_TYPE = "Admin"
    
    # Constructor
    
    def __init__(self, contributorID, firstName, lastName):
        BlogContributor.__init__(self, contributorID, firstName, lastName, BlogAdmin.__CONTRIBUTOR_TYPE)
        self.__permissions = ['create', 'update', 'delete', 'approve', 'publish']
     # public methods
    def showContributorDetails(self):
        BlogContributor.showContributorInformation(self)
        print("permissions:", BlogContributor.getPermissions(self))

class BlogContributorFactory:

    @staticmethod
    def createContributor(contributorType, contributorID, firstName, lastName):
        
        factoryType = {
            "AUTHOR": BlogAuthor,
            "EDITOR": BlogEditor,
            "ADMIN": BlogAdmin
        }
        
        return factoryType[contributorType.upper()](contributorID, firstName, lastName)

# -- DRIVER APPLICATION -----------------------------------------------------

def main():
    
    print("\n*** Start of Program ***\n")    
    
    contributorList = []
    
    contributorType = {
        1:"Author",
        2:"Editor",
        3:"Admin"
    }
    
    while True:
        
        print("1 = " + contributorType[1])
        print("2 = " + contributorType[2])
        print("3 = " + contributorType[3])
        
        menuOption = int(input("Enter Employee Option (1-3) or 0 to exit program: "))
        
        if menuOption == 0:
            print()
            break
        elif menuOption < 0 or menuOption > 3:
            print("ERROR: Invalid option selected!!!!")
            continue
        
        contributorID = input("Enter Contributor ID: ")
        firstName = input("Enter Contributor First Name: ")
        lastName = input("Enter Contributor Last Name: ")
        
        contributorList.append(BlogContributorFactory.createContributor(contributorType[menuOption], contributorID, firstName, lastName))
        
        print()

    print("--- List of Contributors ---")
    for contributor in contributorList:
        print(contributor.getContributorName())
    
    print()
    
    BlogContributor.showNumberOfContributors()
    
    print("\n*** End of Program ***\n")
    
main()