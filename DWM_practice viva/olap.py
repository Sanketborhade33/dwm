CREATE table Time_dw
( time_id int PRIMARY KEY, 
day DATE NOT NULL,
month varchar(255) NOT NULL,
qt varchar(255) NOT NULL,
yr varchar(255) NOT NULL);

INSERT INTO Time_dw(time_id,day, month,qt,yr)
VALUES (101, '2021-01-17', 'january', 'Q1','2021');

INSERT INTO Time_dw(time_id, day,	month,qt,yr)
VALUES (102,  '2021-02-14', 'february', 'Q1','2021');

INSERT INTO Time_dw(time_id, day,	month,qt,yr)  
VALUES (103,  '2021-05-21', 'may', 'Q2','2021');

INSERT INTO Time_dw (time_id, day, month,qt,yr)
VALUES (104,  '2021-06-26', 'june', 'Q2','2021');

select * from Time_dw;
 

CREATE table Product_dw
( prod_id int PRIMARY KEY,
Prod_name varchar(60) NOT NULL,  
Prod_category varchar(255) NOT NULL,  
Brand_name varchar(255) NOT NULL, 
Suppl_name varchar(255) NOT NULL,
Prod_price int );

INSERT INTO product_dw(prod_id,Prod_name,Prod_category,Brand_name, Suppl_name,Prod_price)
VALUES (1, 'rice', 'grocery', 'Dawat','Ramesh',140 );

INSERT INTO product_dw(prod_id,Prod_name,Prod_category,Brand_name, Suppl_name,Prod_price)
VALUES (2, 'Sugar', 'Grocery', 'Dawat','Ramesh',50 );

INSERT INTO Product_dw (prod_id,Prod_name,Prod_category,Brand_name, Suppl_name,  Prod_price)VALUES (3, 'Kurta', 'Cloth', 'Max','Lila',500 );

INSERT INTO product_dw(prod_id,Prod_name,Prod_category,Brand_name, Suppl_name,Prod_price)
VALUES (4, 'jacket', 'Cloth', 'Max','Lila',700 );

select * from product_dw
 

CREATE table Location_dw
(loc_id int PRIMARY KEY,  
street varchar(60) NOT NULL,
city varchar(255) NOT NULL,
state varchar(255) NOT NULL, 
 country varchar(255) NOT NULL);

INSERT INTO Location_dw(loc_id,street,city,state,country)
VALUES (201,'MLROAD','MUMBAI','MAHARASHTRA','INDIA');

INSERT INTO Location_dw(loc_id,street,city,state,country)
VALUES (202,'AIROAD','MUMBAI','MAHARASHTRA','INDIA');

INSERT INTO Location_dw(loc_id,street,city,state,country)
VALUES
(203,'BIROAD','KOLKATA','WESTBENGAL','INDIA');

INSERT INTO Location_dw(loc_id,street,city,state,country)
VALUES (204,'DB ROAD','KOLKATA','WESTBENGAL','INDIA');

select * from Location_dw;
 

CREATE table Fact_sales
(prod_id int REFERENCES Product_dw(prod_id),
time_id int REFERENCES Time_dw(time_id),
loc_id int REFERENCES Location_dw(loc_id),
number_of_unit_sold int NOT NULL,
Total_sales int NOT NULL);

INSERT INTO Fact_sales
(prod_id,time_id,loc_id,number_of_unit_sold,Total_sales)
VALUES (1,104,201,400,90000);
  fact_sales
 
select * from Fact_sales;
 

Roll Up
SELECT yr, SUM(total_sales)
 FROM (Fact_sales NATURAL JOIN  Product_dw)
 JOIN 
 Time_dw ON Fact_sales.time_id=Time_dw.time_id
  GROUP BY yr;
OR
Select Time_dw.yr, sum(total_sales)
From Fact_sales
JOIN Product_dw ON
Fact_sales.product_id =  Product_dw.product_id
JOIN Time_dw ON fact_sales.time_id= time_dw.time_id
Group by time_dw.yr;

Or
Select time.yr, sum(total_sales)
From sales
JOIN product ON
sales.prod_id =  product.prod_id
JOIN time ON sales.time_id= time.time_id
Group by time.yr;

 
Drill Down
SELECT time_dw.qt,SUM(total_sales) 
FROM (Fact_sales NATURAL JOIN  Product_dw)
JOIN Time_dw ON Fact_sales.time_id=Time_dw.time_id  
GROUP BY time_dw.qt;
OR
Select time_dw.qt,sum(total_sales)
From Fact_sales JOIN Product_dw
ON Fact_sales.product_id =  Product_dw.product_id  
JOIN Time_dw ON fact_sales.time_id= time_dw.time_id
Group by time_dw.qt;

OR
Select time_dw.qt,sum(total_sales)
From sales_fact JOIN Product_dw
ON sales_fact.product_id =  Product_dw.product_id  
JOIN Time_dw ON sales_fact.time_id= time_dw.time_id
Group by time_dw.qt;

Or
Select time.qt,sum(total_sales)
From sales JOIN product
ON sales.prod_id =  product.prod_id  
JOIN time ON sales.time_id= time.time_id
Group by time.qt;



 

Pivot
SELECT yr, month,qt
FROM Time_dw as source_table
Or
SELECT yr, month,qt
FROM time as source_table


 

Slice
SELECT Prod_name ,Total_sales
FROM Fact_sales
INNER JOIN Product_dw
ON Fact_sales.prod_id=Product_dw.prod_id

or

SELECT prod_name ,total_sales
FROM sales
INNER JOIN product
ON sales.prod_id=Product.prod_id

 

DICE
SELECT Prod_name ,Total_sales ,day
FROM ((Fact_sales
INNER JOIN Product_dw
ON Fact_sales.prod_id =Product_dw.prod_id) JOIN Time_dw  
ON Fact_sales.time_id =Time_dw.time_id)


Or 
SELECT Product_name ,total_sales ,day
FROM ((sales_fact
INNER JOIN product_dw
ON sales_fact.product_id =product_dw.product_id) JOIN Time_dw  
ON sales_fact.time_id =Time_dw.time_id)

Or
SELECT prod_name ,total_sales ,day
FROM ((sales
INNER JOIN product
ON sales.prod_id =product.prod_id) JOIN time 
ON sales.time_id =time.time_id)

 