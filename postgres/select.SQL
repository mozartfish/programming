-- QUERY SINGLE COLUMN
SELECT 
    first_name
FROM public.customer;

-- QUERY MULTIPLE COLUMNS
SELECT
    first_name,
    last_name,
    email
FROM 
    public.customer;

-- QUERY ALL COLUMNS
SELECT * FROM public.customer

-- QUERY WITH EXPRESSIONS (CONCATENTAION)
SELECT
    first_name ||' ' || last_name,
    EMAIL
FROM
    public.customer;

SELECT 3 * 5;