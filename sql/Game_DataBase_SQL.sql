-- Create Login_Credentials Table
CREATE TABLE Login_Credentials (
    LoginID VARCHAR(50) PRIMARY KEY,
    Email VARCHAR(50),
    Password VARCHAR(50)
);

-- Create Classes Table
CREATE TABLE Classes (
    ClassID VARCHAR(50) PRIMARY KEY,
    ClassType VARCHAR(50),
    SpecialAbilities VARCHAR(50)
);

-- Create WeaponTypes Table
CREATE TABLE WeaponTypes (
    WeaponTypeID VARCHAR(50) PRIMARY KEY,
    Handle VARCHAR(50),
    ClassCompatabilityID INT
);

-- Create WeaponsRarity Table
CREATE TABLE WeaponsRarity (
    WeaponRarityID VARCHAR(50) PRIMARY KEY,
    Rarity VARCHAR(50),
    WeapongDamageRange INT,
    CriticalHitChance INT,
    CriticalDamage INT
);

-- Create ArmorRarity Table
CREATE TABLE ArmorRarity (
    ArmorRarityID VARCHAR(50) PRIMARY KEY,
    Rarity VARCHAR(50),
    PhysicalDefense INT,
    MagicDefense INT,
    Health INT,
    Stamina INT
);

-- Create WeaponAbilities Table
CREATE TABLE WeaponAbilities (
    WeoponAbilityID VARCHAR(50) PRIMARY KEY,
    AbilityDesc VARCHAR(50)
);

-- Create ArmorTypes Table
CREATE TABLE ArmorTypes (
    ArmorTypeID VARCHAR(50) PRIMARY KEY,
    Handle VARCHAR(50),
    ClassCompatabilityID INT
);

-- Create ArmorSpecialAttributes Table
CREATE TABLE ArmorSpecialAttributes (
    AsAID VARCHAR(50) PRIMARY KEY,
    SADescription VARCHAR(50)
);

-- Create ItemTypes Table
CREATE TABLE ItemTypes (
    ItemTypeID VARCHAR(50) PRIMARY KEY,
    Type VARCHAR(50)
);

-- Create Locations Table
CREATE TABLE Locations (
    LocationID VARCHAR(50) PRIMARY KEY,
    LocationName VARCHAR(50),
    Coordinates GEOMETRY
);

-- Create Quests Table
CREATE TABLE Quests (
    QuestsID VARCHAR(50) PRIMARY KEY,
    QuestName VARCHAR(50),
    QuestSteps VARCHAR(50),
    LocationToBegin VARCHAR(50),
    PreRequisiteQuestsID VARCHAR(50),
    FOREIGN KEY (PreRequisiteQuestsID) REFERENCES Quests(QuestsID)
);

-- Create FoodTypes Table
CREATE TABLE FoodTypes (
    FoodTypeID VARCHAR(50) PRIMARY KEY,
    Type VARCHAR(50)
);

-- Create Food Table
CREATE TABLE Food (
    FoodID VARCHAR(50) PRIMARY KEY,
    FoodName VARCHAR(50),
    FoodTypeID VARCHAR(50),
    Effect VARCHAR(50),
    FOREIGN KEY (FoodTypeID) REFERENCES FoodTypes(FoodTypeID)
);

-- Create Faction Table
CREATE TABLE Faction (
    FactionID VARCHAR(50) PRIMARY KEY,
    FactionName VARCHAR(50),
    TotalFactionScore INT,
    NumberOfFactionMembers INT
);

-- Create ItemRarity Table
CREATE TABLE ItemRarity (
    ItemRarityID VARCHAR(50) PRIMARY KEY,
    EffectDurationRange INT
);

-- Create Items Table
CREATE TABLE Items (
    ItemID VARCHAR(50) PRIMARY KEY,
    ItemName VARCHAR(50),
    ItemTypeID VARCHAR(50),
    Effect VARCHAR(50),
    ItemRarityID VARCHAR(50),
    FOREIGN KEY (ItemTypeID) REFERENCES ItemTypes(ItemTypeID),
    FOREIGN KEY (ItemRarityID) REFERENCES ItemRarity(ItemRarityID)
);

-- Create Armors Table
CREATE TABLE Armors (
    ArmorID VARCHAR(50) PRIMARY KEY,
    ArmorName VARCHAR(50),
    ArmorTypeID VARCHAR(50),
    Description VARCHAR(50),
    ArmorRarity VARCHAR(50),
    ArmorStatsID VARCHAR(50),
    LocationIDForDrop VARCHAR(50),
    QuestsIDForDrop VARCHAR(50),
    FOREIGN KEY (ArmorTypeID) REFERENCES ArmorTypes(ArmorTypeID),
    FOREIGN KEY (ArmorRarity) REFERENCES ArmorRarity(ArmorRarityID),
    FOREIGN KEY (ArmorStatsID) REFERENCES ArmorSpecialAttributes(AsAID),
    FOREIGN KEY (LocationIDForDrop) REFERENCES Locations(LocationID),
    FOREIGN KEY (QuestsIDForDrop) REFERENCES Quests(QuestsID)
);

-- Create InventoryArmors Table
CREATE TABLE InventoryArmors (
    InventoryArmorID VARCHAR(50) PRIMARY KEY,
    ArmorID VARCHAR(50),
    FOREIGN KEY (ArmorID) REFERENCES Armors(ArmorID)
);

-- Create InventoryItems Table
CREATE TABLE InventoryItems (
    InventoryItemsID VARCHAR(50) PRIMARY KEY,
    ItemID VARCHAR(50),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

-- Create InventoryFoods Table
CREATE TABLE InventoryFoods (
    InventoryFoodsID VARCHAR(50) PRIMARY KEY,
    FoodID VARCHAR(50),
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID)
);

-- Create Weapons Table
CREATE TABLE Weapons (
    WeaponID VARCHAR(50) PRIMARY KEY,
    WeaponName VARCHAR(50),
    WeaponTypeID VARCHAR(50),
    Description VARCHAR(50),
    WeaponRarityID VARCHAR(50),
    WeaponAbilityID VARCHAR(50),
    LocationIDForDrop VARCHAR(50),
    QuestIDForDrop VARCHAR(50),
    FOREIGN KEY (WeaponTypeID) REFERENCES WeaponTypes(WeaponTypeID),
    FOREIGN KEY (WeaponRarityID) REFERENCES WeaponsRarity(WeaponRarityID),
    FOREIGN KEY (WeaponAbilityID) REFERENCES WeaponAbilities(WeoponAbilityID),
    FOREIGN KEY (LocationIDForDrop) REFERENCES Locations(LocationID),
    FOREIGN KEY (QuestIDForDrop) REFERENCES Quests(QuestsID)
);

-- Create InventoryWeapons Table
CREATE TABLE InventoryWeapons (
    InvenotryWeaponsID VARCHAR(50) PRIMARY KEY,
    WeaponID VARCHAR(50),
    FOREIGN KEY (WeaponID) REFERENCES Weapons(WeaponID)
);

-- Create TradeWeapons Table
CREATE TABLE TradeWeapons (
    TradeWeaponsID VARCHAR(50) PRIMARY KEY,
    WeaponID VARCHAR(50),
    FOREIGN KEY (WeaponID) REFERENCES Weapons(WeaponID)
);

-- Create TradeArmors Table
CREATE TABLE TradeArmors (
    TradeArmorsID VARCHAR(50) PRIMARY KEY,
    ArmorID VARCHAR(50),
    FOREIGN KEY (ArmorID) REFERENCES Armors(ArmorID)
);

-- Create Inventory Table
CREATE TABLE Inventory (
    InventoryID VARCHAR(50) PRIMARY KEY,
    InventoryWepinsID VARCHAR(50),
    InventoryArmorsID VARCHAR(50),
    InvnetoryItemsID VARCHAR(50),
    InventoryFoodsID VARCHAR(50),
    FOREIGN KEY (InventoryWepinsID) REFERENCES InventoryWeapons(InvenotryWeaponsID),
    FOREIGN KEY (InventoryArmorsID) REFERENCES InventoryArmors(InventoryArmorID),
    FOREIGN KEY (InvnetoryItemsID) REFERENCES InventoryItems(InventoryItemsID),
    FOREIGN KEY (InventoryFoodsID) REFERENCES InventoryFoods(InventoryFoodsID)
);

-- Create Player Table
CREATE TABLE Player (
    PlayerID VARCHAR(50) PRIMARY KEY,
    PlayerUserName VARCHAR(50),
    InventoryID VARCHAR(50),
    LoginID VARCHAR(50),
    ClassID VARCHAR(50),
    EXPLevel INT,
    Health INT,
    Gold INT,
    Mana INT,
    Stamina INT,
    PhysicalDefense INT,
    TotalMagicDefenseCap INT,
    FactionID VARCHAR(50),
    PlayerFactionScore INT,
    FOREIGN KEY (InventoryID) REFERENCES Inventory(InventoryID),
    FOREIGN KEY (LoginID) REFERENCES Login_Credentials(LoginID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (FactionID) REFERENCES Faction(FactionID)
);

-- Create Market Table
CREATE TABLE Market (
    ListingID VARCHAR(50) PRIMARY KEY,
    PlayerID VARCHAR(50),
    WeaponID VARCHAR(50),
    ArmorID VARCHAR(50),
    FoodID VARCHAR(50),
    Quantity INT,
    GoldAmount MONEY,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (WeaponID) REFERENCES Weapons(WeaponID),
    FOREIGN KEY (ArmorID) REFERENCES Armors(ArmorID),
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID)
);

-- Create Trades Table
CREATE TABLE Trades (
    TradeID VARCHAR(50) PRIMARY KEY,
    PlayerID VARCHAR(50),
    TradeWeaponsID VARCHAR(50),
    TradeArmorsID VARCHAR(50),
    Gold_Amount MONEY,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (TradeWeaponsID) REFERENCES TradeWeapons(TradeWeaponsID),
    FOREIGN KEY (TradeArmorsID) REFERENCES TradeArmors(TradeArmorsID)
);
