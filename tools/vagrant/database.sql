-- Create database (drop it if it's already there)
DROP DATABASE IF EXISTS freedomvote;
DROP ROLE IF EXISTS freedomvote;

CREATE USER freedomvote WITH SUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN PASSWORD 'vagrant';
CREATE DATABASE freedomvote WITH TEMPLATE = template0 OWNER = freedomvote;
