-- ORIGINAL QUERY
SELECT
    first_name,
    last_name
FROM public.customer;

-- ALIAS QUERY
SELECT 
    first_name,
    last_name AS surname
FROM public.customer;

-- ALIAS QUERY ALTERNATIVE
SELECT
    first_name,
    last_name surname
FROM public.customer;

-- CONCATENTATION
SELECT
    first_name || ' ' || last_name
FROM public.customer;

-- CONCATENTATION ALIAS
SELECT
    first_name || ' ' || last_name AS full_name
FROM public.customer;

-- SPACE ALIASES
SELECT
    first_name || ' ' || last_name AS "full name"
FROM 
    public.customer;