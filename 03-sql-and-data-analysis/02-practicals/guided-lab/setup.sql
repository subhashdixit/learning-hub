CREATE TABLE customers(id INTEGER PRIMARY KEY,name TEXT NOT NULL);
CREATE TABLE orders(id INTEGER PRIMARY KEY,customer_id INTEGER,amount INTEGER,status TEXT,day TEXT);
INSERT INTO customers VALUES(1,'Asha'),(2,'Ben'),(3,'Chen'),(4,'Diya');
INSERT INTO orders VALUES(1,1,100,'paid','2026-01-01'),(2,1,50,'paid','2026-01-02'),(3,2,80,'refunded','2026-01-01'),(4,2,200,'paid','2026-01-03'),(5,3,NULL,'pending','2026-01-02'),(6,3,100,'paid','2026-01-04');
