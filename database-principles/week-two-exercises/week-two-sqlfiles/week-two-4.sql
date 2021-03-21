USE MyGuitarShop

SELECT ProductName
      , ListPrice
      , DiscountPercent, ListPrice * (DiscountPercent * .01) AS DiscountAmount, ListPrice - (ListPrice * (DiscountPercent * .01)) AS DiscountPrice
  FROM Products

GO


