-- this is a comment 
-- this is a second comment

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost';
GRANT select ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;