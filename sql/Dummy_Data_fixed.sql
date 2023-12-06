-- Inserting dummy data into Login_Credentials
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
INSERT INTO Items (ItemID, ItemName, Rarity, Type, LocationID, QuestID)
VALUES 
    (1, 'Sword', 'Rare', 'Weapon', 1, NULL),
    (2, 'Potion', 'Common', 'Consumable', 3, NULL),
    (3, 'Spellbook', 'Epic', 'Artifact', NULL, 2);

-- Inserting dummy data into Player
INSERT INTO Player (Playerid, Username, ClassID, Health, Gold, Mana, Level, FactionID)
VALUES 
    (1, 'user1', 1, 100, 50, 80, 5, 1),
    (2, 'user2', 2, 80, 30, 120, 3, 1),
    (3, 'user3', 3, 120, 70, 60, 7, 1),
    (4, 'user4', 1, 90, 40, 100, 4, 2),
    (5, 'user5', 3, 110, 60, 90, 6, 2);

-- Inserting dummy data into Inventory
INSERT INTO Inventory (Playerid, ItemID)
VALUES 
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 1),
    (4, 2),
    (5, 3);

INSERT INTO Trade (BelongsTo, ItemToTradeID, ItemNeedID)
VALUES
    (1, 1, 3),
    (2, 2, 1),
    (3, 1, 2);
  
