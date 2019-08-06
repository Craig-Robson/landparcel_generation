# landparcel generation
Generate landparcels (constellations of land) from Ordnance Survey MasterMap

## Description
Working with PostgreSQL and PostGIS this takes a table with Ordnance Survey Topographic area polygons (pre-assigned to areas) and performs spatial methods to produce a set of landparcels. These are defined as blocks of land which are bounded completely by physical features, isolating the area into single landparcel. The output of the operation, the landparcels, are written to a database table.

Written in python.

## Dependencies
- python 2.7+
- psycopg2
