USE MyWebDB;

INSERT INTO dbo.Users (EmailAddress, FirstName, LastName) VALUES ('bill@yahoo.com', 'Bill', 'Stevenson'), ('steve@yahoo.com', 'Steve', 'Stevenson'); 


INSERT INTO dbo.Products (ProductName) VALUES('Potato'), ('Onion');

INSERT INTO dbo.Downloads (DownloadDate, FileName) VALUES ( GETDATE(), 'my file'),
( GETDATE(), 'my file'),
(GETDATE(), 'my file');

SELECT EmailAddress as email_address,
FirstName as first_name, 
LastName as last_name, 
DownloadDate as download_date, 
ProductName as product_name, 
ProductName as product_name FROM dbo.Users, dbo.Products, dbo.Downloads ORDER BY EmailAddress, ProductName;