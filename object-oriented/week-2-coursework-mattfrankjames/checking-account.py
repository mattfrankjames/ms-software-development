class CheckingAccount:
    def __init__(self, accountId, firstName, lastName, address, city, state, zipCode):
        self.__accountId = accountId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode
        self.__balance = 0
        self.__error = False
        
    # Private methods
    def __credit(self, amount):
        self.__balance = self.__balance + abs(amount)
        self.__printTransactionMessage('Credit')
        
    def __debit(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - abs(amount)
            self.__printTransactionMessage('Debit')
        else:
            self.__printInsufficientFundsMessage(amount)
            
            
    def __printTransactionMessage(self, message):
        if self.__error == False:
            print('{} transaction processed'.format(message))
        else:
            print('ERROR: Transaction not processed\n"{}" is not a valid transaction type'.format(message))
            
    def __printInsufficientFundsMessage(self, amount):
        print('ERROR: The debit amount ${:.2f} is more than your account balance'.format(amount))
        
    # Public methods
    
    def processTransaction(self, type, amount):
        if type.upper() == 'CREDIT':
            self.__credit(amount)
        elif type.upper() == 'DEBIT':
            self.__debit(amount)
        else:
            self.__error = True
            self.__printTransactionMessage(type)
            self.__error = False
    
    def printBalance(self):
        return 'Account {} has a balance of ${:.2f} \n'.format(self.__accountId, self.__balance)

    
    def getBalance(self):
        return self.__balance
    
def main():
    checkingAccount = CheckingAccount('45678', 'Matt', 'James', '443 Oak St.', 'St. Louis', 'MO', '63119')
    
    checkingAccount.processTransaction('credit', 1000.00)
    print(checkingAccount.printBalance())
    
    
    checkingAccount.processTransaction('debit', 50.00)
    print(checkingAccount.printBalance())
    
    checkingAccount.processTransaction('credit', 300.90)
    print(checkingAccount.printBalance())
    
    checkingAccount.processTransaction('bacon', 45.00)
    print(checkingAccount.printBalance())
    
    checkingAccount.processTransaction('debit', 500.00)
    print(checkingAccount.printBalance())
    
    checkingAccount.processTransaction('debit', 800.00)
    print(checkingAccount.printBalance())
    
main()
    
        
        
                        
        