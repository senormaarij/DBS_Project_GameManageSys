SELECT 
    Weapons.WeaponName,
    Armors.ArmorName,
    Items.ItemName,
    Food.FoodName
FROM 
    Player
JOIN 
    Inventory ON Player.InventoryID = Inventory.InventoryID
LEFT JOIN 
    InventoryWeapons ON Inventory.InventoryWepinsID = InventoryWeapons.InvenotryWeaponsID
LEFT JOIN 
    Weapons ON InventoryWeapons.WeaponID = Weapons.WeaponID
LEFT JOIN 
    InventoryArmors ON Inventory.InventoryArmorsID = InventoryArmors.InventoryArmorID
LEFT JOIN 
    Armors ON InventoryArmors.ArmorID = Armors.ArmorID
LEFT JOIN 
    InventoryItems ON Inventory.InvnetoryItemsID = InventoryItems.InventoryItemsID
LEFT JOIN 
    Items ON InventoryItems.ItemID = Items.ItemID
LEFT JOIN 
    InventoryFoods ON Inventory.InventoryFoodsID = InventoryFoods.InventoryFoodsID
LEFT JOIN 
    Food ON InventoryFoods.FoodID = Food.FoodID
WHERE 
    Player.PlayerID = 'player1';
