-- Maps
INSERT INTO apex_maps (name) VALUES ("Kings Canyon");
INSERT INTO apex_maps (name) VALUES ("World's Edge");
INSERT INTO apex_maps (name) VALUES ("Olympus");

-- POIs Kings Canyon
SET @map_name = "Kings Canyon";

INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Slum Lakes", 0);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Pit", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Containment", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Runoff", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Artillery", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Bunker", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Airbase", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Gauntlet", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Salvage", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Mirage Voyage", 0);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Market", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Water Treatment", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Cage", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Map Room", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Repulsor", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Hydro Dam", 0);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Labs", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Swamps", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Rig", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Capacitor", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Crash Site", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Spotted Lake", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Broken Relay", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Caustic Treatment", 1);

-- POIs Olympus
SET @map_name = "Olympus";
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Docks", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Carrier", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Oasis", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Power Grid", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Turbine", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Rift", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Energy Depot", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Gardens", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Grow Towers", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Hammond Labs", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Estates", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Elysium", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Hydroponics", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Bonsai Plaza", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Solar Array", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Orbital Cannon", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Fight Night", 1);

-- World's Edge
SET @map_name = "World's Edge";
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Trials", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Skyhook", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Countdown", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Lava Fissure", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Train Yard", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Survey Camp", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Epicenter", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Refinery", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Fragment West", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Fragment East", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Overlook", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Geyser", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Harvester", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Staging", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Thermal Station", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Storting Factory", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Tree", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Launch Site", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"The Dome", 1);
INSERT INTO apex_pois (id_maps,name,enabled) VALUES ((SELECT id FROM apex_maps WHERE name = @map_name),"Lava City", 1);