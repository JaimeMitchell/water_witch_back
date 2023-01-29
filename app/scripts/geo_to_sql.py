import pandas as pd
import geopandas as gpd
from geoalchemy2 import Geometry, WKTElement
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import JSONB, ARRAY, HSTORE, INTEGER, base
from psycopg2 import *
from shapely.geometry import GeometryCollection, Point
from osgeo_utils import gdal_merge, gdal_edit, gdal_calc, ogrmerge
import fiona
fiona.supported_drivers

# the alchemy that makes all this turn into SQL, make tables and dbs. Honestly, I'm not convinced this process is easier than just using SQL.
engine = create_engine(
    'db://na:na@port:0000/no')

# Read file and make a Geo Data Frame of the file I want to change.
gdf = gpd.read_file('nycdf.geoJson')

# I know it's free and all, but I don't care for the names of open source columns. However, when I tried to give the geo dtype,'geography', a new name, from pandas, this broke the entire program. Not sure why other than spatial data is a bit more finicky than other d-types.
renamed_gdf = gdf.rename(columns={'signname': 'name', 'position': 'details'})

# Spring cleaning for data. This took a 10.6 MB file and spit out a 880 kb minime version.
gdf = renamed_gdf.filter(['geometry', 'name', 'details', 'borough'])

# Just wanted to make different file formats from this one that is cleaned up.
gdf.to_file('filteredNYC.geoJson', driver='GeoJSON')
gdf.to_file('filteredNYC.shp')
gdf.to_csv('filteredNYC.csv')

# Copy the DataFrame into my table. name='table name', con=SQLalchemy converts this mess into SQL and copies it into the db, if_exists==the table is there, overwrite it, index==Need that id,primary key? Yes please, chunksize==how many rows you want?, dtype==this column i'm naming needs to be this kind of datatype. This part is how I make the geojson geography/geometry columns compatible with postgres, SRID of 4326, which is the standard for WGS 84 (latitude-longitude) coordinates.
gdf.to_postgis(name='fountains', con=engine, if_exists='replace', index=True,
               index_label='id', chunksize=None, dtype={'geometry': Geometry('POINT', srid=4326)})

# prints the first 5 instead of 5000
print(gdf.head())
