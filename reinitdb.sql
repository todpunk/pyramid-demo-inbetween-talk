

DROP TABLE IF EXISTS models;

CREATE TABLE models (
	id           bigserial PRIMARY KEY,
	name         text NOT NULL,
	value        INTEGER NOT NULL                   -- There's actually no readon for these to be NOT NULL, but they are'
);

INSERT INTO models (name, value) VALUES ('one', 1);
INSERT INTO models (name, value) VALUES ('two', 2);
