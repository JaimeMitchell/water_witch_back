import pandas as pd
import geopandas as gpd
from shapely import wkt

# Read CSV file and make a Geo Data Frame of the file I want to change.
gdf = gpd.read_file("modified.csv")

# Load a geometry from a WKT string. Convert the "POINT" column to a geometry.
gdf["geometry"] = gdf["POINT"].apply(wkt.loads)
#A GeoDataFrame object is a pandas.DataFrame that has a column with geometry.
#  Coordinate Reference System of the geometry objects. 
gdf = gpd.GeoDataFrame(gdf, geometry='geometry')
# A GeoDataFrame object is a pandas DataFrame that has a column with geometry.

# Extract the latitude and longitude
gdf["latitude"] = gdf.geometry.y
gdf["longitude"] = gdf.geometry.x

# Drop the POINT column from the schema/model
gdf = gdf.drop("POINT", axis=1)

# Convert the GeoDataFrame back to a CSV file, rename it "fountains".
gdf.to_csv("fountain.csv", index_label='id')

