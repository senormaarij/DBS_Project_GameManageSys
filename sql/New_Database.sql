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
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(100),
    Rarity VARCHAR(100),
    Type VARCHAR(100),
    LocationID INT REFERENCES Locations(LocationID),
    QuestID INT REFERENCES Quests(QuestsID)
);

CREATE TABLE Player (
    Playerid INT PRIMARY KEY,
    Username VARCHAR(100) REFERENCES Login_Credentials(Username),
    ClassID INT REFERENCES Classes(ClassID),
    Health INT,
    Gold INT,
    Mana INT,
    Level INT,
    FactionID INT REFERENCES Faction(FactionID)
);

CREATE TABLE Inventory (
    Playerid INT REFERENCES Player(Playerid),
    ItemID INT REFERENCES Items(ItemID),
    PRIMARY KEY (Playerid, ItemID)
);


CREATE TABLE Trade (
    TradeID int PRIMARY KEY IDENTITY(1,1),
    BelongsTo int REFERENCES Player(Playerid),
    ItemToTradeID int REFERENCES Items(ItemID),
    ItemNeedID int REFERENCES Items(ItemID)
);
