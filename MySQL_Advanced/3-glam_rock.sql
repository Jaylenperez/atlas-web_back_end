-- List Glam rock bands ranked by longevity (formed/split are YEAR integers)

SELECT band_name, 
       CASE
           WHEN split IS NULL THEN YEAR(CURDATE()) - formed  -- Use current year if split is NULL
           ELSE split - formed
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;