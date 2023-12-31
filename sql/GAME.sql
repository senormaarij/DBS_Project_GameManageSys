CREATE TABLE Login_Credentials (
    Username VARCHAR(100) PRIMARY KEY,
    Email VARCHAR(100),
    Password VARCHAR(100)
);

CREATE TABLE Faction (
    FactionID INT PRIMARY KEY,
    FactionName VARCHAR(100),
    TotalFactionScore INT,
    NumebrOfFactionMembers INT
);

CREATE TABLE Classes (
    ClassID INT PRIMARY KEY,
    ClassType VARCHAR(100),
    SpecialAbilites VARCHAR(100)
);

CREATE TABLE Locations (
    LocationID INT PRIMARY KEY,
    LocationName VARCHAR(100),
    Co_ordinates GEOMETRY
);

CREATE TABLE Quests (
    QuestsID INT PRIMARY KEY,
    QuestName VARCHAR(100),
    QuestSteps VARCHAR(100),
    LocationToBegin INT REFERENCES Locations(LocationID),
    PreRequisiteQuestsID INT REFERENCES Quests(QuestsID)
);

CREATE TABLE Items (
    ItemID INT IDENTITY(1,1)PRIMARY KEY,
    ItemName VARCHAR(100),
    Rarity VARCHAR(100),
    Type VARCHAR(100),
    LocationID INT REFERENCES Locations(LocationID),
    QuestID INT REFERENCES Quests(QuestsID)
);

CREATE TABLE Player (
    PlayerID INT IDENTITY(1,1) PRIMARY KEY,
    Username VARCHAR(100) REFERENCES Login_Credentials(Username),
    ClassID INT REFERENCES Classes(ClassID),
    Health INT,
    Gold INT,
    Mana INT,
    Level INT,
    FactionID INT REFERENCES Faction(FactionID)
);

CREATE TABLE Inventory (
    Playerid INT REFERENCES Player(PlayerID),
    ItemID INT REFERENCES Items(ItemID),
    PRIMARY KEY (Playerid, ItemID)
);


CREATE TABLE Trade (
    TradeID int IDENTITY(1,1) PRIMARY KEY,
    BelongsTo int REFERENCES Player(PlayerID),
    ItemToTradeID int REFERENCES Items(ItemID),
    ItemNeedID int REFERENCES Items(ItemID)
);

CREATE TABLE Market_Item (
    ItemID int PRIMARY KEY REFERENCES Items(ItemID),
    Gold int
);

 
INSERT INTO Login_Credentials (Username, Email, Password)
VALUES 
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2'),
    ('user3', 'user3@example.com', 'password3'),
    ('user4', 'user4@example.com', 'password4'),
    ('user5', 'user5@example.com', 'password5');

-- Inserting dummy data into Faction
INSERT INTO Faction (FactionID, FactionName, TotalFactionScore, NumebrOfFactionMembers)
VALUES 
    (1, 'Faction1', 1000, 3),
    (2, 'Faction2', 800, 2);

-- Inserting dummy data into Classes
INSERT INTO Classes (ClassID, ClassType, SpecialAbilites)
VALUES 
    (1, 'Warrior', 'Strength Boost'),
    (2, 'Mage', 'Spellcasting Mastery'),
    (3, 'Rogue', 'Stealth and Agility');

-- Inserting dummy data into Locations
INSERT INTO Locations (LocationID, LocationName, Co_ordinates)
VALUES 
    (1, 'Castle', 'POINT(0 0)'),
    (2, 'Forest', 'POINT(10 20)'),
    (3, 'Cave', 'POINT(-5 -10)');

-- Inserting dummy data into Quests
INSERT INTO Quests (QuestsID, QuestName, QuestSteps, LocationToBegin, PreRequisiteQuestsID)
VALUES 
    (1, 'Rescue the Princess', 'Save the princess from the castle', 1, NULL),
    (2, 'Hunt the Dragon', 'Defeat the dragon in the forest', 2, 1);

-- Inserting dummy data into Items
INSERT INTO Items (ItemName, Rarity, Type, LocationID, QuestID)
VALUES 
    ('Sword', 'Rare', 'Weapon', 1, NULL),
    ('Healing Potion', 'Common', 'Consumable', 3, NULL),
    ('Spellbook', 'Epic', 'Artifact', NULL, 2),
	('Sword', 'Legendary', 'Weapon', 2, NULL),
	('Axe', 'Common', 'Weapon', NULL, NULL),
    ('Bow', 'Rare', 'Weapon', NULL, NULL),
    ('Leather Armor', 'Common', 'Armour', NULL, NULL),
    ('Magic Wand', 'Epic', 'Artifact', NULL, 1),
    ('Potion of Invisibility', 'Legendary', 'Consumable', NULL, NULL),
    ('Hammer', 'Common', 'Weapon', NULL, NULL);


-- Inserting dummy data into Player
INSERT INTO Player (Username, ClassID, Health, Gold, Mana, Level, FactionID)
VALUES 
    ('user1', 1, 100, 50, 80, 5, 1),
    ('user2', 2, 80, 30, 120, 3, 1),
    ('user3', 3, 120, 70, 60, 7, 1),
    ('user4', 1, 90, 40, 100, 4, 2),
    ('user5', 3, 110, 60, 90, 6, 2);

-- Inserting dummy data into Inventory
INSERT INTO Inventory (Playerid, ItemID)
VALUES 
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
	(2, 2),
    (2, 4),
    (2, 5),
	(3, 1),
    (3, 3),
    (3, 5),
	(4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5),
	(5, 1),
    (5, 3);

INSERT INTO Trade (BelongsTo, ItemToTradeID, ItemNeedID)
VALUES
    (1, 1, 3),
    (2, 2, 1),
    (3, 1, 2);
  
INSERT INTO Market_Item (ItemID, Gold)
VALUES 
    (1, 50),   
    (2, 20),   
    (3, 80),
    (4, 30),
    (5, 15),
    (6, 25),
    (7, 10),
    (8, 35),
    (9, 45),
    (10, 40); 

select * from Login_Credentials
select * from Classes 
select * from Faction
select * from Inventory 
select * from Items 
select * from Locations 
select * from Market_Item 
select * from Player 
select * from Quests
select * from Trade
	