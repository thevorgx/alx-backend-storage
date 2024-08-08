-- reset email value by a trigger
-- default = 0
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
    SET NEW.valid_email = IF(OLD.email != NEW.email, DEFAULT, NEW.valid_email);
