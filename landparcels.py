import psycopg2
from psycopg2 import sql


def database_connection(db_params):
    """Establish a database connection
    """
    # create connection to the database
    connection = psycopg2.connect("dbname=%s user=%s port=%s host=%s password=%s" %(db_params['database_name'], db_params['user'], db_params['port'], db_params['host'], db_params['password']))

    return connection


def main(area_codes, output_table, database_connection_parameters):
    """

    area_codes = a list of area codes to run the query for
    output_table = the table in the database to store the output of the query in

    OS MasterMap feature codes:
    10089 = rivers
    10172 = roads
    10183 = roadside
    10185 = structure (e.g.bridge)
    10167 = rail
    """

    # establish a database connection and return a cursor object and connection object
    connection = database_connection(database_connection_parameters)

    # create cursor
    cursor = connection.cursor()

    # run the query
    # loop through the areas
    for area_code in area_codes:
        cursor.execute(sql.SQL('INSERT INTO {0} SELECT(ST_Dump(ST_Difference(st_union(oas.geom), (SELECT st_union(wkb_geometry) as the_geom FROM topographicarea WHERE (lad=%s) and (featurecode = 10089 OR featurecode = 10172 OR featurecode = 10183 OR featurecode = 10185 OR featurecode = 10167 ))))).geom FROM ftables.oa_withareas as oas WHERE oas.lad_code = %s;').format(sql.Identifier(output_table)), [area_code, area_code])

        # commit query results to the database
        connection.commit()

    return
