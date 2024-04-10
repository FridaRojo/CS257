DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quakedate text,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magError real,
  locationSource text,
  mageSource text,
  place text
);
