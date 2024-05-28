CREATE TABLE IF NOT EXISTS customers(
  id serial PRIMARY KEY,
  first_name VARCHAR (50) NOT NULL,
  last_name VARCHAR (50) NOT NULL,
  email VARCHAR (300) UNIQUE NOT NULL);
