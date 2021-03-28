Use MyWebDB;

ALTER TABLE Products
ADD ProductPrice INT NOT NULL;

ALTER TABLE Products
ADD CHECK (ProductPrice >= 9.99);

ALTER TABLE Productd
ADD DateAdded SMALLDATETIME NOT NULL;