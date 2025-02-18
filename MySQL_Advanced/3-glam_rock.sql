-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, 
       (YEAR(split) - YEAR(formed)) AS lifespan 
FROM metal_bands 
WHERE main_style = 'Glam rock' 
ORDER BY lifespan DESC;
