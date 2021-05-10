
-- Create the database
CREATE DATABASE BikeRaces;

GO

-- Create the tables for organizing body, athlete, offical, series and race
CREATE TABLE OrganizingBody (OrgID INT PRIMARY KEY, Name VARCHAR(50) NOT NULL, Location VARCHAR(50) NOT NULL);

CREATE TABLE Athlete (LicenseNumber INT PRIMARY KEY, FirstName VARCHAR(50) NOT NULL, LastName VARCHAR(50) NOT NULL, 
category VARCHAR(50), OverallRanking INT NULL, OrgID INT REFERENCES OrganizingBody (OrgID) NULL);

CREATE TABLE Official (OfficialLicense INT PRIMARY KEY, FirstName VARCHAR(50) NOT NULL, LastName VARCHAR(50) NOT NULL,
OrgID INT REFERENCES OrganizingBody (OrgID) NULL);

CREATE TABLE Series (SeriesID INT PRIMARY KEY, OrgID INT REFERENCES OrganizingBody (OrgID) NULL, SeriesName VARCHAR(50) NOT NULL);

CREATE TABLE Race (PermitNumber INT PRIMARY KEY, Name VARCHAR(50), OrgID INT REFERENCES OrganizingBody (OrgID) NULL,
Date DATETIME NOT NULL, PrizeMoney FLOAT NULL, OfficialLicense INT REFERENCES Official (OfficialLicense), SeriesID INT REFERENCES Series (SeriesID));

-- Race and Series have a many to many relationship, this is the intermediate table to handle that.

CREATE TABLE RacesSeries (RaceID INT NOT NULL REFERENCES Race(PermitNumber), SeriesID INT NOT NULL REFERENCES Series(SeriesID), PRIMARY KEY(RaceId, SeriesID)); 

-- Populate tables with data

INSERT INTO OrganizingBody (OrgID, Name, Location) VALUES (1, 'UsaCycling', 'Colorado Springs'),
	(2, 'UFD', 'St. Charles, MO'), 
	(3, 'UCI', 'Aigle, Switzerland'), 
	(4, 'WORS', 'Wisconsin'),
	(5, 'DINO', 'Indiana');
INSERT INTO Athlete (LicenseNumber, FirstName, LastName, category, OverallRanking, OrgID) VALUES (123, 'Matt', 'James', 'Category 1', 100, 1),
	(345, 'Daniel', 'Miller', 'Category 1', 1, 3),
	(456, 'Dave', 'Breslin', 'Category 1', 15, 4),
	(567, 'Christopher', 'Connolly', 'Category 2', 80, 5),
	(678, 'Devin', 'Clark', 'Pro', 2, 3);
INSERT INTO Official (OfficialLicense, FirstName, LastName, OrgID) VALUES (45, 'Martin', 'Lang', 1),
	(89, 'Marijn', 'Rodney', 3),
	(56, 'Larry', 'Martin', 1),
	(67, 'Valerie', 'Salazar', 2),
	(78, 'Sara', 'Rodney', 3);
INSERT INTO Series VALUES (1, 1, 'USAProTour'),
	(2, 1, 'United Federation of Dirt'),
	(3, 2, 'UCI World Cup'),
	(4, 4, 'Wisonsin Off Road Series'),
	(5, 5, 'Indiana MTB Cup');
INSERT INTO Race VALUES (42, 'Lost Valley Luau', 1, 2021-08-23, 1000.00, 45, 1), 
	(33, 'Greensfelder Challenge', 2, 2021-05-27,2000.00, 56, 2),
	(12, 'Castlewood Cup', NULL, 2021-06-30, 1500.00, 45, 2),
	(66, 'Brown County Breakdown', 4, 2021-07-15, 5000.00, 67, 3),
	(98, 'Tsali Tsunami', 5, 2021-06-16, 3000.00, 78, 4);

INSERT INTO RacesSeries VALUES (98, 4), (98, 5), (66, 2), (66, 3), (33, 2), (12, 2);

-- Create specific views

CREATE VIEW TopRacers AS SELECT
TOP 3 OverallRanking FROM Athlete
ORDER BY OverallRanking DESC;

CREATE VIEW TopPrizeMoney AS SELECT 
TOP 3 PrizeMoney FROM Race
ORDER BY PrizeMoney DESC;

CREATE VIEW SharedOrg AS SELECT 
Race.Name, Series.SeriesName, Race.OrgId FROM Series
JOIN Race ON Race.OrgId = Series.OrgID

CREATE VIEW OfficialMultipleRaces AS SELECT
Official.FirstName, Official.LastName, Race.Name, Official.OfficialLicense FROM Official
JOIN Race ON Official.OfficialLicense = Race.OfficialLicense

CREATE VIEW OrgMultipleRaces AS SELECT
OrganizingBody.OrgID, Race.Name, Race.Date, Race.SeriesID
FROM OrganizingBody JOIN Race ON OrganizingBody.OrgID = Race.OrgID


SELECT Race.SeriesID, Series.SeriesName, Race.PrizeMoney, SUM(Race.PrizeMoney) TotalPrizeMoney FROM RACE 
JOIN Series ON Race.SeriesID = Series.SeriesID
GROUP BY Race.PrizeMoney, Race.SeriesID, Series.SeriesName
ORDER BY Race.PrizeMoney DESC;

SELECT FirstName, LastName, category, OverallRanking FROM Athlete
WHERE OverallRanking < 80
ORDER BY OverallRanking;

-- create a stored procedure that makes a copy of the organizing body table

CREATE PROC spOrgBodyCopy
AS IF OBJECT_ID('OrgBodyCopy') IS NOT NULL
	DROP Table OrgBodyCopy
SELECT * INTO OrgBodyCopy 
FROM OrganizingBody

-- Query to access the many to many relationship between the race and series tables

SELECT Race.Name, Race.PermitNumber, Race.PrizeMoney, Race.SeriesID FROM Race
JOIN RacesSeries ON Race.PermitNumber = RacesSeries.RaceID JOIN Series ON RacesSeries.SeriesID = Series.SeriesID