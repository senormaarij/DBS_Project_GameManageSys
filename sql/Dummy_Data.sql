

-- Insert dummy data into Login_Credentials Table
INSERT INTO Login_Credentials (LoginID, Email, Password)
VALUES 
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2');

-- Insert dummy data into Classes Table
INSERT INTO Classes (ClassID, ClassType, SpecialAbilities)
VALUES 
    ('class1', 'Warrior', 'Strength Boost'),
    ('class2', 'Mage', 'Fireball Spell');

-- Insert dummy data into WeaponTypes Table
INSERT INTO WeaponTypes (WeaponTypeID, Handle, ClassCompatabilityID)
VALUES 
    ('1', 'Sword', 1),
    ('2', 'Staff', 2);

-- Insert dummy data into WeaponsRarity Table
INSERT INTO WeaponsRarity (WeaponRarityID, Rarity, WeapongDamageRange, CriticalHitChance, CriticalDamage)
VALUES 
    ('1', 'Common', 10, 5, 2),
    ('2', 'Rare', 15, 10, 5);

-- Insert dummy data into ArmorRarity Table
INSERT INTO ArmorRarity (ArmorRarityID, Rarity, PhysicalDefense, MagicDefense, Health, Stamina)
VALUES 
    ('1', 'Common', 20, 10, 5, 5),
    ('2', 'Rare', 30, 20, 10, 10);

-- Insert dummy data into WeaponAbilities Table
INSERT INTO WeaponAbilities (WeoponAbilityID, AbilityDesc)
VALUES 
    ('ability1', 'Slash Attack'),
    ('ability2', 'Fireball');

-- Insert dummy data into ArmorTypes Table
INSERT INTO ArmorTypes (ArmorTypeID, Handle, ClassCompatabilityID)
VALUES 
    ('1', 'Plate', 1),
    ('2', 'Robe', 2);

-- Insert dummy data into ArmorSpecialAttributes Table
INSERT INTO ArmorSpecialAttributes (AsAID, SADescription)
VALUES 
    ('stats1', 'Heavy and Durable'),
    ('stats2', 'Magical Protection');

-- Insert dummy data into ItemTypes Table
INSERT INTO ItemTypes (ItemTypeID, Type)
VALUES 
    ('1', 'Potion'),
    ('2', 'Scroll');

-- Insert dummy data into Locations Table
INSERT INTO Locations (LocationID, LocationName, Coordinates)
VALUES 
    ('location1', 'Forest', 'POINT(1 1)'),
    ('location2', 'Castle', 'POINT(2 2)');

-- Insert dummy data into Quests Table
INSERT INTO Quests (QuestsID, QuestName, QuestSteps, LocationToBegin, PreRequisiteQuestsID)
VALUES 
    ('quest1', 'Journey into the Forest', 'Explore the depths of the forest', 'location1', NULL),
    ('quest2', 'Retrieve the Magic Scroll', 'Find the scroll in the castle', 'location2', 'quest1');

-- Insert dummy data into FoodTypes Table
INSERT INTO FoodTypes (FoodTypeID, Type)
VALUES 
    ('1', 'Fruit'),
    ('2', 'Meat');

-- Insert dummy data into Food Table
INSERT INTO Food (FoodID, FoodName, FoodTypeID, Effect)
VALUES 
    ('food1', 'Apple', '1', 'Health +5'),
    ('food2', 'Steak', '2', 'Stamina +10');

-- Insert dummy data into Faction Table
INSERT INTO Faction (FactionID, FactionName, TotalFactionScore, NumberOfFactionMembers)
VALUES 
    ('faction1', 'Knights of the Round Table', 1000, 50),
    ('faction2', 'Mages Guild', 1200, 40);

-- Insert dummy data into ItemRarity Table
INSERT INTO ItemRarity (ItemRarityID, EffectDurationRange)
VALUES 
    ('rarity1', 5),
    ('rarity2', 10);

-- Insert dummy data into Items Table
INSERT INTO Items (ItemID, ItemName, ItemTypeID, Effect, ItemRarityID)
VALUES 
    ('item1', 'Healing Potion', '1', 'Heals 20 HP', 'rarity1'),
    ('item2', 'Fireball Scroll', '2', 'Unleashes a fireball', 'rarity2');

-- Insert dummy data into Armors Table
INSERT INTO Armors (ArmorID, ArmorName, ArmorTypeID, Description, ArmorRarity, ArmorStatsID, LocationIDForDrop, QuestsIDForDrop)
VALUES 
    ('armor1', 'Iron Plate', '1', 'Heavy iron armor', '1', 'stats1', 'location1', 'quest1'),
    ('armor2', 'Mage Robe', '2', 'Enchanted mage robe', '2', 'stats2', 'location2', 'quest2');

-- Insert dummy data into InventoryArmors Table
INSERT INTO InventoryArmors (InventoryArmorID, ArmorID)
VALUES 
    ('inv_armor1', 'armor1'),
    ('inv_armor2', 'armor2');

-- Insert dummy data into InventoryItems Table
INSERT INTO InventoryItems (InventoryItemsID, ItemID)
VALUES 
    ('inv_item1', 'item1'),
    ('inv_item2', 'item2');

-- Insert dummy data into InventoryFoods Table
INSERT INTO InventoryFoods (InventoryFoodsID, FoodID)
VALUES 
    ('inv_food1', 'food1'),
    ('inv_food2', 'food2');

-- Insert dummy data into Weapons Table
INSERT INTO Weapons (WeaponID, WeaponName, WeaponTypeID, Description, WeaponRarityID, WeaponAbilityID, LocationIDForDrop, QuestIDForDrop)
VALUES 
    ('weapon1', 'Sword of Valor', '1', 'A powerful sword', '1', 'ability1', 'location1', 'quest1'),
    ('weapon2', 'Staff of Wisdom', '2', 'A wise staff', '2', 'ability2', 'location2', 'quest2');

-- Insert dummy data into InventoryWeapons Table
INSERT INTO InventoryWeapons (InvenotryWeaponsID, WeaponID)
VALUES 
    ('inv_weapon1', 'weapon1'),
    ('inv_weapon2', 'weapon2');

-- Insert dummy data into TradeWeapons Table
INSERT INTO TradeWeapons (TradeWeaponsID, WeaponID)
VALUES 
    ('trade_weapon1', 'weapon1'),
    ('trade_weapon2', 'weapon2');

-- Insert dummy data into TradeArmors Table
INSERT INTO TradeArmors (TradeArmorsID, ArmorID)
VALUES 
    ('trade_armor1', 'armor1'),
    ('trade_armor2', 'armor2');

-- Insert dummy data into Player Table
INSERT INTO Player (PlayerID, PlayerUserName, InventoryID, LoginID, ClassID, EXPLevel, Health, Gold, Mana, Stamina, PhysicalDefense, MagicDefense, FactionID, PlayerFactionScore)
VALUES 
    ('player1', 'HeroicWarrior', 'inventory1', 'user1', 'class1', 10,100, 500, 100, 200, 150,150, 'faction1', 500),
    ('player2', 'MysticMage', 'inventory2', 'user2', 'class2', 8, 120, 300, 80, 120, 80,150, 'faction2', 400);



-- Insert dummy data into Market Table
INSERT INTO Market (ListingID, PlayerID, WeaponID, ArmorID, FoodID, Quantity, GoldAmount)
VALUES 
    ('market_listing1', 'player1', 'weapon1', 'armor1', 'food1', 5, 100),
    ('market_listing2', 'player2', 'weapon2', 'armor2', 'food2', 3, 80);

-- Insert dummy data into Trades Table
INSERT INTO Trades (TradeID, PlayerID, TradeWeaponsID, TradeArmorsID, Gold_Amount)
VALUES 
    ('trade1', 'player1', 'trade_weapon1', 'trade_armor1', 50),
    ('trade2', 'player2', 'trade_weapon2', 'trade_armor2', 75);

-- Insert dummy data into Inventory Table
INSERT INTO Inventory (InventoryID, InventoryWepinsID, InventoryArmorsID, InvnetoryItemsID, InventoryFoodsID)
VALUES 
    ('inventory1', 'inv_weapon1', 'inv_armor1', 'inv_item1', 'inv_food1'),
    ('inventory2', 'inv_weapon2', 'inv_armor2', 'inv_item2', 'inv_food2');

select * from Login_Credentials
select * from Inventory
select* from Faction
select* from player
select* from Market
select* from ArmorRarity
select* from Armors
select* from ArmorSpecialAttributes
select* from ArmorTypes
select* from Classes
select* from Food
select * from FoodTypes
select* from InventoryArmors
select* from InventoryFoods
select* from InventoryWeapons
select * from ItemRarity
select* from Items
select* from ItemTypes
select* from Locations
select* from Quests

