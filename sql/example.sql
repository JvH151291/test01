DROP TABLE IF EXISTS daniehei;

-- Init table
CREATE TABLE daniehei(
	NAME varchar PRIMARY KEY,
	AGE smallint
);

-- Copy from file
-- for windows user specify the path as follows
-- \copy daniehei( NAME, AGE ) FROM 'C:\\Users\\daniehei\\gitlab\\PuvIntro\\sql\\daniehei.csv' delimiter ';' CSV HEADER;
-- for unix users
\copy daniehei( NAME, AGE ) FROM '~/gitlab/PuvIntro/sql/daniehei.csv' delimiter ';' CSV HEADER;