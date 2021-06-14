-- SELECT ORDERING
SELECT
    first_name,
    last_name
FROM 
    public.customer
ORDER BY
    first_name ASC;


-- LAST NAME DESC
SELECT
    first_name,
    last_name
FROM 
    public.customer
ORDER BY
    last_name DESC;


-- ORDER BY MULTIPLE COLUMNS
SELECT 
    first_name,
    last_name
FROM 
    customer
ORDER BY
    first_name ASC,
    last_name DESC;

-- ORDER BY EXPRESSIONS
SELECT
    first_name,
    LENGTH(first_name) AS len
FROM
    public.customer
ORDER BY 
    len DESC;


-- NULLS ORDERING
CREATE TABLE sort_demo(
    num INT
);

INSERT INTO sort_demo(num)
VALUES(1),(2),(3),(null);

SELECT num
FROM sort_demo
ORDER BY num;

SELECT num
FROM sort_demo
ORDER BY num NULLS LAST;

SELECT num
FROM sort_demo
ORDER BY num NULLS FIRST;

SELECT num
FROM sort_demo
ORDER BY num DESC;

SELECT num
FROM sort_demo
ORDER BY num NULLS LAST;