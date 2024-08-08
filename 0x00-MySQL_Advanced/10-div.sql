-- function SafeDiv that divides a / b, return 0 if b = 0
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
RETURN IF(b = 0, 0, a / b);
