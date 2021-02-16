SELECT map.name, poi.name, mapoi.id
FROM apex_maps AS map,
apex_pois AS poi,
apex_map_poi AS mapoi
WHERE map.id = mapoi.id_maps 
AND poi.id = mapoi.id_pois
AND mapoi.enabled = 1;