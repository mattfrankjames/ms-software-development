import json

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
    itemNameToInventory = {}
    for inventoryFileName in inventoryFileNames: 
        inventoryFile = open(inventoryFileName, 'r')
        
        inventoryData = json.loads(inventoryFile.read())
        
        
        contents = inventoryData['contents']
        for content in contents:
            
            for slot in content['slots']:
                
                itemName = slot['item_name']
                inventoryItem = itemNameToInventory.get( itemName, InventoryItem( itemName ) )
                inventoryItem.addToStocked(slot['last_stock'])
                inventoryItem.addToInStock(slot['current_stock'])
                inventoryItem.incrementSlots()
                itemNameToInventory[itemName] = inventoryItem
            
    cokeItem = itemNameToInventory['Coke']
    print( cokeItem )
    print( cokeItem.getNumberSold() )
    print( cokeItem.getSoldPct() * 100 )
    print( cokeItem.getStockNeed() )
    
    sortChoice = ''
    inventoryItemsList = list( itemNameToInventory.values() )
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
        
        
        print()
        
main()