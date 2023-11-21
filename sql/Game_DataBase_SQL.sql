-- Create Login_Credentials Table
CREATE TABLE Login_Credentials (
    LoginID VARCHAR PRIMARY KEY,
    Email VARCHAR,
    Password VARCHAR
);

-- Create Classes Table
CREATE TABLE Classes (
    ClassID VARCHAR PRIMARY KEY,
    ClassType VARCHAR,
    SpecialAbilities VARCHAR
);





-- Create Wepons Table done




-- Create WeponTypes Table done
CREATE TABLE WeponTypes (
    WeponTypeID VARCHAR PRIMARY KEY,
    Handle VARCHAR,
    ClassCompatabilityID INT
);

-- Create WeponsRarity Table done
CREATE TABLE WeponsRarity (
    WeponRarityID VARCHAR PRIMARY KEY,
    Rarity VARCHAR,
    WepongDamageRange INT,
    CriticalHitChance INT,
    CriticalDamage INT
);

-- Create ArmorRarity Table done
CREATE TABLE ArmorRarity (
    ArmorRarityID VARCHAR PRIMARY KEY,
    Rarity VARCHAR,
    PhysicalDefense INT,
    MagicDefense INT,
    Health INT,
    Stamina INT
);

-- Create WeponAbilities Table done
CREATE TABLE WeponAbilities (
    WeoponAbilityID VARCHAR PRIMARY KEY,
    AbilityDesc VARCHAR
);

-- Create ArmorTypes Table done
CREATE TABLE ArmorTypes (
    ArmorTypeID VARCHAR PRIMARY KEY,
    Handle VARCHAR,
    ClassCompatabilityID INT
);

-- Create ArmorSpecialAttributes Table done
CREATE TABLE ArmorSpecialAttributes (
    AsAID VARCHAR PRIMARY KEY,
    SADescription VARCHAR
);




-- Create ItemTypes Table done
CREATE TABLE ItemTypes (
    ItemTypeID VARCHAR PRIMARY KEY,
    Type VARCHAR
);



-- Create Locations Table done
CREATE TABLE Locations (
    LocationID VARCHAR PRIMARY KEY,
    LocationName VARCHAR,
    Coordinates GEOMETRY
);

-- Create Quests Table done
CREATE TABLE Quests (
    QuestsID VARCHAR PRIMARY KEY,
    QuestName VARCHAR,
    QuestSteps VARCHAR,
    LocationToBegin VARCHAR,
    PreRequisiteQuestsID VARCHAR,
    FOREIGN KEY (PreRequisiteQuestsID) REFERENCES Quests(QuestsID)
);

-- Create FoodTypes Table done
CREATE TABLE FoodTypes (
    FoodTypeID VARCHAR PRIMARY KEY,
    Type VARCHAR
);

-- Create Food Table done
CREATE TABLE Food (
    FoodID VARCHAR PRIMARY KEY,
    FoodName VARCHAR,
    FoodTypeID VARCHAR,
    Effect VARCHAR,
    FOREIGN KEY (FoodTypeID) REFERENCES FoodTypes(FoodTypeID)
);

-- Create Faction Table done
CREATE TABLE Faction (
    FactionID VARCHAR PRIMARY KEY,
    FactionName VARCHAR,
    TotalFactionScore INT,
    NumberOfFactionMembers INT
);



-- Create ItemRarity Table done
CREATE TABLE ItemRarity (
    ItemRarityID VARCHAR PRIMARY KEY,
    EffectDurationRange INT
);

-- Create Items Table done
CREATE TABLE Items (
    ItemID VARCHAR PRIMARY KEY,
    ItemName VARCHAR,
    ItemTypeID VARCHAR,
    Effect VARCHAR,
    ItemRarityID VARCHAR,
    FOREIGN KEY (ItemTypeID) REFERENCES ItemTypes(ItemTypeID),
    FOREIGN KEY (ItemRarityID) REFERENCES ItemRarity(ItemRarityID)
);




CREATE TABLE Armors (
    ArmorID VARCHAR PRIMARY KEY,
    ArmorName VARCHAR,
    ArmorTypeID VARCHAR,
    Description VARCHAR,
    ArmorRarity VARCHAR,
    ArmorStatsID VARCHAR,
    LocationIDForDrop VARCHAR,
    QuestsIDForDrop VARCHAR,
    FOREIGN KEY (ArmorTypeID) REFERENCES ArmorTypes(ArmorTypeID),
    FOREIGN KEY (ArmorRarity) REFERENCES ArmorRarity(ArmorRarityID),
    FOREIGN KEY (ArmorStatsID) REFERENCES ArmorSpecialAttributes(AsAID),
    FOREIGN KEY (LocationIDForDrop) REFERENCES Locations(LocationID),
    FOREIGN KEY (QuestsIDForDrop) REFERENCES Quests(QuestsID)
);

-- Create InventoryArmors Table done
CREATE TABLE InventoryArmors (
    InventoryArmorID VARCHAR PRIMARY KEY,
    ArmorID VARCHAR,
    FOREIGN KEY (ArmorID) REFERENCES Armors(ArmorID)
);

-- Create InventoryItems Table
CREATE TABLE InventoryItems (
    InventoryItemsID
	VARCHAR PRIMARY KEY,
    ItemID VARCHAR,
	FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

-- Create InventoryFoods Table done
CREATE TABLE InventoryFoods (
    InventoryFoodsID VARCHAR PRIMARY KEY,
    FoodID VARCHAR,
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID)
);

CREATE TABLE Wepons (
    WeponID VARCHAR PRIMARY KEY,
    WeponName VARCHAR,
    WeponTypeID VARCHAR,
    Description VARCHAR,
    WeponRarityID VARCHAR,
    WeponAbilityID VARCHAR,
    LocationIDForDrop VARCHAR,
    QuestIDForDrop VARCHAR,
    FOREIGN KEY (WeponTypeID) REFERENCES WeponTypes(WeponTypeID),
    FOREIGN KEY (WeponRarityID) REFERENCES WeponsRarity(WeponRarityID),
    FOREIGN KEY (WeponAbilityID) REFERENCES WeponAbilities(WeoponAbilityID),
    FOREIGN KEY (LocationIDForDrop) REFERENCES Locations(LocationID),
    FOREIGN KEY (QuestIDForDrop) REFERENCES Quests(QuestsID)
);

-- Create InventoryWepons Table done
CREATE TABLE InventoryWepons (
    InvenotryWeponsID VARCHAR PRIMARY KEY,
    WeponID VARCHAR,
    FOREIGN KEY (WeponID) REFERENCES Wepons(WeponID)
);

-- Create TradeWepons Table done
CREATE TABLE TradeWepons (
    TradeWeponsID VARCHAR PRIMARY KEY,
    WeponID VARCHAR,
    FOREIGN KEY (WeponID) REFERENCES Wepons(WeponID)
);

-- Create TradeArmors Table done
CREATE TABLE TradeArmors (
    TradeArmorsID VARCHAR PRIMARY KEY,
    ArmorID VARCHAR,
    FOREIGN KEY (ArmorID) REFERENCES Armors(ArmorID)
);

-- Create Armors Table done



-- Create Inventory Table done
CREATE TABLE Inventory (
    InventoryID VARCHAR PRIMARY KEY,
    InventoryWepinsID VARCHAR,
    InventoryArmorsID VARCHAR,
    InvnetoryItemsID VARCHAR,
    InventoryFoodsID VARCHAR,
    FOREIGN KEY (InventoryWepinsID) REFERENCES InventoryWepons(InvenotryWeponsID),
    FOREIGN KEY (InventoryArmorsID) REFERENCES InventoryArmors(InventoryArmorID),
    FOREIGN KEY (InvnetoryItemsID) REFERENCES InventoryItems(InventoryItemsID),
    FOREIGN KEY (InventoryFoodsID) REFERENCES InventoryFoods(InventoryFoodsID)
);

-- Create Player Table done
CREATE TABLE Player (
    PlayerID VARCHAR PRIMARY KEY,
    PlayerUserName VARCHAR,
    InventoryID VARCHAR,
    LoginID VARCHAR,
    ClassID VARCHAR,
    EXPLevel INT,
    EXPfor_next_level INT,
    Gold MONEY,
    TotalManaCap INT,
    TotalStaminaCap INT,
    TotalPhysicalDefenseCap INT,
    TotalMagicDefenseCap INT,
    FactionID VARCHAR,
    PlayerFactionScore INT,
    FOREIGN KEY (InventoryID) REFERENCES Inventory(InventoryID),
    FOREIGN KEY (LoginID) REFERENCES Login_Credentials(LoginID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID),
    FOREIGN KEY (FactionID) REFERENCES Faction(FactionID)
);

-- Create Market Table done
CREATE TABLE Market (
    ListingID VARCHAR PRIMARY KEY,
    PlayerID VARCHAR,
    WeponID VARCHAR,
    ArmorID VARCHAR,
    FoodID VARCHAR,
    Quantity INT,
    GoldAmount MONEY,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (WeponID) REFERENCES Wepons(WeponID),
    FOREIGN KEY (ArmorID) REFERENCES Armors(ArmorID),
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID)
);

-- Create Trades Table
CREATE TABLE Trades (
    TradeID VARCHAR PRIMARY KEY,
    PlayerID VARCHAR,
    TradeWeponsID VARCHAR,
    TradeArmorsID VARCHAR,
    Gold_Amount MONEY,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID),
    FOREIGN KEY (TradeWeponsID) REFERENCES TradeWepons(TradeWeponsID),
    FOREIGN KEY (TradeArmorsID) REFERENCES TradeArmors(TradeArmorsID)
);