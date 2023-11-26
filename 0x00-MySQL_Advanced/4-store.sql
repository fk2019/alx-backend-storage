-- trigger to decrease quantity of an item after
-- new order is added
CREATE TRIGGER order_trigger
AFTER INSERT ON `orders`
FOR EACH ROW
UPDATE 	 `items` SET `quantity` = `quantity` - NEW.number
WHERE `name` = NEW.item_name;
