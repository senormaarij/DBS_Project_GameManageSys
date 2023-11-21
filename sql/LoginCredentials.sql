CREATE TABLE LoginCredentials (
  Email varchar(255) DEFAULT NULL,
  playerID varchar(10) DEFAULT NULL,
  password varchar(255) DEFAULT NULL,
  PRIMARY KEY (playerID)
);


-- Dumping data for table user_details


INSERT INTO LoginCredentials (Email, playerID, password) VALUES
('user1@example.com', 'player123', 'password123'),
('user2@example.com', 'player456', 'securePass456'),
('user3@example.com', 'player789', 'secretWord789'),
('user4@example.com', 'player234', 'myPassword123')


select * from LoginCredentials