-- create users table with id, unique email, name
-- and country with enum attribute
CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
PRIMARY KEY(id)
);
