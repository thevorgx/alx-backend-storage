-- find glam rock bands and rank them by life span
-- (use 2022 if split is null)
SELECT
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
