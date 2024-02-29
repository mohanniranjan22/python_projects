-- CREATE DATABASE IF NOT EXISTS railway_reservation_system;

-- USE railway_reservation_system;

-- CREATE TABLE IF NOT EXISTS trains (
--     train_id INT AUTO_INCREMENT PRIMARY KEY,
--     train_name VARCHAR(100) NOT NULL,
--     source VARCHAR(100) NOT NULL,
--     destination VARCHAR(100) NOT NULL,
--     total_seats INT NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS reservations (
--     reservation_id INT AUTO_INCREMENT PRIMARY KEY,
--     train_id INT,
--     user_name VARCHAR(100) NOT NULL,
--     num_tickets INT NOT NULL,
--     FOREIGN KEY (train_id) REFERENCES trains(train_id)
-- );

CREATE TABLE IF NOT EXISTS users(
    user_name VARCHAR(100) NOT NULL,
    user_password VARCHAR(30) NOT NULL
);
