CREATE TABLE cache_table (
    cache_key character varying(255) NOT NULL,
    value text NOT NULL,
    expires timestamp with time zone NOT NULL
);

ALTER TABLE cache_table OWNER TO postgres;

COPY cache_table (cache_key, value, expires) FROM stdin;
\.

ALTER TABLE ONLY cache_table
    ADD CONSTRAINT cache_table_pkey PRIMARY KEY (cache_key);

CREATE INDEX cache_table_expires ON cache_table USING btree (expires);
