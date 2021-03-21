USE MyGuitarShop

SELECT LastName + ' ,' + FirstName as 'Full Name'
  FROM Customers WHERE LastName BETWEEN 'M' AND 'Z'

ORDER BY LastName 



