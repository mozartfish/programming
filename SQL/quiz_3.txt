-- 1 CALCULATE AGE
SELECT
    first_name,
    EXTRACT(YEAR FROM AGE(birth_date)) AS age
FROM public.person;

-- 2 MULTIPLY AGE
SELECT
    first_name,
    EXTRACT(YEAR FROM AGE(birth_date)) AS age,
    -- EXTRACT(YEAR FROM AGE(birth_date)) * 100 AS age_100x,
    (EXTRACT(YEAR FROM AGE(birth_date)) * study_group) / 100 AS score
FROM public.person;

-- 3 GENERATE NEW ID'S
SELECT
 CONCAT(SUBSTRING(first_name, 1,  POSITION(' ' IN first_name) - 1), ' ', SUBSTRING(id, POSITION('-' in id) + 1)) AS new_id,
    id,
    LENGTH(id) AS id_length,
    POSITION('-' in id) AS end_of_person_id,
    SUBSTRING(id, POSITION('-' in id) + 1) AS second_id,
    first_name AS full_name,
    Length(first_name) AS name_length,
    POSITION(' ' IN first_name) AS end_of_first_name,
    SUBSTRING(first_name, 1,  POSITION(' ' IN first_name) - 1) as first_id
FROM public.person;

-- 4 CALCULATE RANK
SELECT
    first_name,
    EXTRACT(YEAR FROM AGE(birth_date)) AS age,
    -- EXTRACT(YEAR FROM AGE(birth_date)) * 100 AS age_100x,
    (EXTRACT(YEAR FROM AGE(birth_date)) * study_group) / 100 AS score,
    CASE WHEN (EXTRACT(YEAR FROM AGE(birth_date)) * study_group) / 100 >= 1.0 THEN 'gold star'
        WHEN (EXTRACT(YEAR FROM AGE(birth_date)) * study_group) / 100 < 1.0 
             AND (EXTRACT(YEAR FROM AGE(birth_date)) * study_group) / 100 >= 0.4 THEN 'bronze star'
        ELSE 'no star'
        END AS rank
FROM public.person;

-- 5 CONCATENATE STUDY_GROUP SQUARED AND COLOR
SELECT
    study_group,
    favorite_color,
    POWER(study_group, 2) AS study_group_squared,
    CONCAT(POWER(study_group, 2), '_', favorite_color) AS group_color_squared
FROM public.person;