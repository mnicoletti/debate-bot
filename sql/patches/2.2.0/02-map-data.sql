SET @map_name = "Olympus";
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Icarus", 1);

SET @map_name = "World's Edge";
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Climatizer", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Lava Pool", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Landslide", 1);

UPDATE apex_pois SET enabled = 0 WHERE name = "Train Yard";
UPDATE apex_pois SET enabled = 0 WHERE name = "Storting Factory";
UPDATE apex_pois SET enabled = 0 WHERE name = "Refinery";