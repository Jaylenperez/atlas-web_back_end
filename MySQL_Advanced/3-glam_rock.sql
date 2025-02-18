-- List Glam rock bands ranked by longevity, handling NULL split dates

SELECT band_name, 
       CASE
           WHEN split IS NULL THEN YEAR(CURDATE()) - YEAR(formed)  -- Use current year if split is NULL
           ELSE YEAR(split) - YEAR(formed)
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;