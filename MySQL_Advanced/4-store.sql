-- Create a trigger that decreases item quantity after adding a new order

DELIMITER $$

CREATE TRIGGER trg_orders_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity of the ordered item
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;