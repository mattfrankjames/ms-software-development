# question one
USE MyGuitarShop

SELECT ProductCode, ProductName, DiscountPercent, ListPrice
  FROM Products

ORDER BY ListPrice DESC

#question two
USE MyGuitarShop

SELECT LastName + ' ,' + FirstName as 'Full Name'
  FROM Customers WHERE LastName BETWEEN 'M' AND 'Z'

ORDER BY LastName



#question three
USE MyGuitarShop

SELECT ProductName, ListPrice, DateAdded FROM Products WHERE ListPrice BETWEEN 500 AND 2000

ORDER BY DateAdded DESC



#question four
USE MyGuitarShop

SELECT ProductName
      , ListPrice
      , DiscountPercent, ListPrice * (DiscountPercent * .01) AS DiscountAmount, ListPrice - (ListPrice * (DiscountPercent * .01)) AS DiscountPrice
  FROM Products

GO


#question five
USE MyGuitarShop

SELECT ItemID
	, ItemPrice
	, DiscountAmount
	, Quantity, ItemPrice * Quantity AS PriceTotal
	, DiscountAmount * Quantity AS DiscountTotal
	, (ItemPrice - DiscountAmount) * Quantity AS ItemTotal
  FROM OrderItems WHERE ((ItemPrice - DiscountAmount) * Quantity) > 500
  ORDER BY ((ItemPrice - DiscountAmount) * Quantity) DESC



#question six
USE MyGuitarShop

SELECT OrderID
      , OrderDate
      , ShipDate
  FROM Orders WHERE ShipDate IS NULL



#question seven
Use MyGuitarShop

SELECT Price = 100, TaxRate = .07, 100 * .07 AS TaxAmount, 100 + (100 * .07) AS Total

