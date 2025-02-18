-- List Glam rock bands ranked by longevity

SELECT band_name, (YEAR(split) - YEAR(formed)) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;