# Game Inventory Management System

A desktop-based game inventory management system developed using **Python, PyQt6, and Microsoft SQL Server**.

The project simulates how an online game can manage player-related data such as inventories, items, player accounts, trades, factions, quests, locations, and an in-game marketplace through a relational database.

The application provides a graphical interface through which players can log in, view their inventory, search for items, trade with other players, and purchase items from the marketplace.

---

## Features

### Player Management
- Player registration and login
- Player health, mana, gold, and level tracking
- Player class and faction information
- Login credential management

### Inventory Management
- View a player's current inventory
- Display item name, rarity, and type
- Search inventory by item name
- Filter items by rarity
- Filter items by item type

### Trading System
- View available player-to-player trades
- Create a trade by selecting an item from the player's inventory
- Select an item wanted in exchange
- Validate whether the required item is available
- Complete trades by exchanging items between inventories
- Prevent players from trading with themselves
- Prevent players from acquiring duplicate items

### Marketplace
- Browse items available for purchase
- Display item name, rarity, type, and price
- Purchase items using in-game gold
- Prevent purchases when the player does not have enough gold
- Prevent players from purchasing items they already own
- Automatically update the player's inventory and gold after a successful purchase

### Multiplayer / Player Interaction
- View other players' trades
- View players belonging to the same faction
- Interact with the trading system through the multiplayer interface

---

## Technologies Used

- **Python**
- **PyQt6** – Graphical user interface
- **Microsoft SQL Server** – Relational database
- **pyodbc** – Python database connectivity
- **Qt Designer** – GUI design and `.ui` files
- **SQL** – Database schema, queries, and data manipulation

---

## System Overview

The application is divided into two main layers:

### Graphical User Interface

The user interface is designed using Qt Designer and stored in `.ui` files. These interfaces are loaded by the Python application at runtime.

The main interfaces include:

- `Login.ui` – Login and registration
- `Inventory.ui` – Player inventory and player information
- `Multiplayer.ui` – Trading and faction interaction
- `Trade Confirm.ui` – Creating a new trade
- `Market.ui` – In-game marketplace

### Application Logic

`main.py` handles the application's functionality and connects the GUI to the SQL database.

The application uses `pyodbc` to establish a connection with Microsoft SQL Server and executes SQL queries for retrieving and modifying game data.

---

## Database Design

The database models several components of an online game's data system.

### Database Entities

| Table | Purpose |
|---|---|
| `Login_Credentials` | Stores player usernames, emails, and passwords |
| `Player` | Stores player statistics and relationships to classes and factions |
| `Inventory` | Associates players with the items they own |
| `Items` | Stores item information such as name, rarity, type, location, and associated quest |
| `Trade` | Stores player-created item trade requests |
| `Market_Item` | Stores items available in the marketplace and their gold prices |
| `Faction` | Stores faction information and faction statistics |
| `Classes` | Stores available player classes and their special abilities |
| `Quests` | Stores quests, their steps, starting locations, and prerequisites |
| `Locations` | Stores locations within the game world |

---

## Entity Relationships

The database uses foreign keys to connect the different parts of the game system.

### Player

A `Player` is connected to:

- `Login_Credentials` through the player's username
- `Classes` through `ClassID`
- `Faction` through `FactionID`
- `Inventory` through `PlayerID`

Player information includes:

- Health
- Mana
- Gold
- Level
- Class
- Faction

### Inventory and Items

The `Inventory` table acts as a relationship between players and items.

Each inventory record connects:

```text
PlayerID → ItemID
