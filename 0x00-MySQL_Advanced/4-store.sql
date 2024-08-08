-- trigger that decrease the quantity of an item when its ordered
CREATE TRIGGER decrease_qt
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
