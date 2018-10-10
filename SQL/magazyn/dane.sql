DROP TABLE IF EXISTS dane_customers;
CREATE TABLE dane_customers
(
    customers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    address TEXT
);

DROP TABLE IF EXISTS dane_orders;
CREATE TABLE dane_orders
(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date DATE,
    FOREIGN KEY (dane_customers_id) REFERENCES dane_customers(id),
    FOREIGN KEY (dane_subscriptions_id) REFERENCES dane_subscriptions(id),
);

DROP TABLE IF EXISTS dane_subscriptions;
CREATE TABLE dane_subscriptions
(
    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description    TEXT,
    price_per_month INTEGER,
    subscription_length TEXT
);
