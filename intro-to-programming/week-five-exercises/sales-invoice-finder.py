salesFile = open('sales_data.csv', 'r')
searchTerm = ''
searchTotalRecords = 0
nameOrId = ''
while True:
    nameOrId = input('Search by invoice id (id) or customer last name (lname)? ')
    if nameOrId == 'id' or nameOrId == 'lname':
        searchTerm = input('Enter your search term: ')
        break
    else:
        print('ERROR: You much enter either \'id\' for id search or \'lname\' for customer last name search')


for line in salesFile:
    if (nameOrId == 'id' and searchTerm == line.split(',')[0]) or searchTerm.capitalize() == line.split(',')[2]:
        searchTotalRecords += 1
salesFile.close()   

print('{0} records found'.format(searchTotalRecords))

        