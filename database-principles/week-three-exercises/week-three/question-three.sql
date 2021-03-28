USE MyWebDB;

INSERT INTO Users VALUES (34987, 'bill@yahoo.com', 'Bill', 'Stevenson'); 
INSERT INTO Users VALUES (23487, 'steve@yahoo.com', 'Steve', 'Stevenson');

INSERT INTO Products VALUES(56709, 'Potato');
INSERT INTO Products VALUES(34529, 'Onion');

INSERT INTO Downloads VALUES(345, 34987, GETDATE(), 'my file', 34529);
INSERT INTO Downloads VALUES(345, 23487, GETDATE(), 'my file', 56709);
INSERT INTO Downloads VALUES(345, 23487, GETDATE(), 'my file', 34529);

SELECT EmailAddress as email_address,
FirstName as first_name, 
LastName as last_name, 
DownloadDate as download_date, 
ProductName as product_name, 
ProductName as product_name FROM Users, Products, Downloads ORDER BY EmailAddress, ProductName;