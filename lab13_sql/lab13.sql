.read data.sql

-- QUESTIONS --



-------------------------------------------------------------------------
------------------------ Give Interest- ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
UPDATE accounts
SET amount = amount * 1.02;


create table give_interest_result as select * from accounts; -- just for tests

-------------------------------------------------------------------------
------------------------ Split Accounts ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
CREATE TABLE accounts_temp AS
  SELECT accounts.name || "'s Savings account" AS name, accounts.amount * 0.5 AS amount
  FROM accounts;
INSERT INTO accounts_temp
  SELECT accounts.name || "'s Checking account", accounts.amount * 0.5
  FROM accounts;
DROP TABLE accounts;
CREATE TABLE accounts AS
  SELECT * FROM accounts_temp;



create table split_account_results as select * from accounts; -- just for tests

-------------------------------------------------------------------------
-------------------------------- Whoops ---------------------------------
-------------------------------------------------------------------------

-- replace this line with your solution
DROP TABLE accounts;


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) as average_price
  FROM products
  GROUP BY category;

CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) AS price
  FROM inventory
  GROUP BY item;

CREATE TABLE shopping_list AS
  SELECT name, store FROM (
    SELECT products.name, MAX(products.rating / products.MSRP), lowest_prices.store
    FROM products, lowest_prices
    WHERE products.name = lowest_prices.item
    GROUP BY products.category
  );

CREATE TABLE total_bandwidth AS
  SELECT SUM(stores.Mbs)
  FROM shopping_list, stores
  WHERE shopping_list.store = stores.store;