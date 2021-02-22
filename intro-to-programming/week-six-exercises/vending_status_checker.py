import json

class MachineStatus:
    def __init__(self, machineLabel):
        self.machineLabel = machineLabel
        self.totalBeverages = 0
        self.totalInStock = 0
        self.moneyEarned = 0
        self.numberSoldPerSlot = 0
    def addToStocked(self, stockAmount):
        self.totalBeverages = self.totalBeverages + stockAmount
    def addToInStock(self, inStockAmount):
        self.totalInStock = self.totalInStock + inStockAmount
    def getNumberSold(self):
        return self.totalBeverages - self.totalInStock
    def getSoldPct(self):
        return (self.getNumberSold() / self.totalBeverages) * 100
    def getMoneyEarnedPerSlot(self, price):
        return self.numberSoldPerSlot * price
    def getTotalSales(self):
        return self.moneyEarned
    def getName(self):
        return self.machineLabel
    def __repr__(self):
        return 'Machine Name: {}, last stocked total: {},  current stock: {}, money: {}'.format(self.machineLabel, self.totalBeverages, self.totalInStock, self.moneyEarned)

class InventoryItem:
    def __init__(self, itemName):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0
        
    def addToStocked(self, stockAmount):
        self.totalStocked = self.totalStocked + stockAmount
    def addToInStock(self, inStockAmount):
        self.totalInStock = self.totalInStock + inStockAmount
    def incrementSlots(self):
        self.totalSlots = self.totalSlots + 1
    def getNumberSold(self):
        return self.totalStocked - self.totalInStock
    def getSoldPct(self):
        return self.getNumberSold() / self.totalStocked
    def getStockNeed(self):
        return 8 * self.totalSlots - self.totalInStock
    def getName(self):
        return self.name
    def getNumberInStock(self):
        return self.totalInStock
    def __repr__(self):
        return '{} In Stock: {}, Stock {}, Slots {}'.format(self.name, self.totalInStock, self.totalStocked, self.totalSlots)
    
def main():
    inventoryFileNames = ['REID_1F_20171004.json', 'REID_2F_20171004.json', 'REID_3F_20171004.json']
    machineToInventory = {}
        
    itemNameToInventory = {}
    
    
    for inventoryFileName in inventoryFileNames: 
        inventoryFile = open(inventoryFileName, 'r')
        
        inventoryData = json.loads(inventoryFile.read())
    
        
        contents = inventoryData['contents']
        machineLabel = inventoryData['machine_label']
        machineInventory = machineToInventory.get( machineLabel, MachineStatus( machineLabel ))
       
        for content in contents:
            
            for slot in content['slots']:
                
                itemName = slot['item_name']
                inventoryItem = itemNameToInventory.get( itemName, InventoryItem( itemName ) )
                inventoryItem.addToStocked(slot['last_stock'])
                inventoryItem.addToInStock(slot['current_stock'])
                inventoryItem.incrementSlots()
                itemNameToInventory[itemName] = inventoryItem
                
                machineInventory.addToStocked(slot['last_stock'])
                machineInventory.addToInStock(slot['current_stock'])
                machineInventory.numberSoldPerSlot = slot['last_stock'] - slot['current_stock']
                earnedPerSlot = machineInventory.getMoneyEarnedPerSlot(slot['item_price'])
                machineInventory.moneyEarned = machineInventory.moneyEarned + earnedPerSlot
            
        machineToInventory[machineLabel] = machineInventory
    
    sortChoice = ''
    inventoryItemsList = list( itemNameToInventory.values() )
    
    machinesList = list( machineToInventory.values() )
    
    reportChoice = input('Would you like the (m)achine report or the (i)nventory report? ').lower()
    
    if reportChoice == 'i':  
        while sortChoice != 'q':
            sortChoice = input('Sort by (n)ame, (p)ct sold, (s)tocking need, or (q) to quit: ')
            if sortChoice == 'n':
                inventoryItemsList.sort( key=InventoryItem.getName )
            elif sortChoice == 'p':
                inventoryItemsList.sort( key=InventoryItem.getSoldPct )
                inventoryItemsList.reverse()
            elif sortChoice == 's':
                inventoryItemsList.sort( key=InventoryItem.getStockNeed )
            
            print('Item Name            Sold     % Sold     In Stock Stock needs')
            for item in inventoryItemsList:
                print( '{:20} {:8} {:8.2f}% {:8} {:8}'.format( item.getName(), item.getNumberSold(), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
    elif reportChoice == 'm':
        print('Label       Pct Sold     Sales Total')
        for machine in machinesList:
            print( '{:8} {:8.2f}% ${:10.2f}'.format(machine.getName(), machine.getSoldPct(), machine.getTotalSales()))
        
main()