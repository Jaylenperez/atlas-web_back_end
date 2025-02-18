-- List all bands with Glam rock as their main style, ranked by longevity

SELECT band_name, 
       CASE
           WHEN split IS NULL THEN YEAR(CURDATE()) - formed  -- Calculate lifespan if band is still active
           ELSE split - formed                                -- Calculate lifespan if band is split
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'  -- Use LIKE to handle variations like 'Glam rock,...'
ORDER BY lifespan DESC;