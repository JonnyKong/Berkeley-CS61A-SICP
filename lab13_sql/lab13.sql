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
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE lowest_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE shopping_list AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
