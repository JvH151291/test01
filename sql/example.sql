DROP TABLE IF EXISTS daniehei;

-- Init table
CREATE TABLE daniehei(
	NAME varchar PRIMARY KEY,
	AGE smallint
);

-- Copy from file
\copy daniehei( NAME, AGE ) FROM '~/gitlab/PuvIntro/sql/daniehei.csv' delimiter ';' CSV HEADER;