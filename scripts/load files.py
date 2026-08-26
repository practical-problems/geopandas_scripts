import os
import geopandas

file_path = input("What is the file path? \n").strip()
gdf = geopandas.read_file(file_path)
saveName = input("What the name of the file to save as? \n").strip()
driverSelectionInput = input("What driver? Input a number only\n 1. GPKG \n 2. ESRI Shapefile \n 3. GeoJSON \n 4. FlatGeobuf \n 5. GeoJSONSeq \n 6.SQLite \n 7. Others")
match driverSelectionInput:
    case "1":
        driverSelection = "GPKG"
    case "2":
        driverSelection = "ESRI Shapefile"
    case "3":
        driverSelection = "GeoJSON"
    case "4":
        driverSelection = "FlatGeobuf"
    case "5":
        driverSelection = "GeoJSONSeq"
    case "6":
        driverSelection = "SQLite"
    case "7":
        driverSelection = input("Then type in which drivers".strip())
gdf.to_file(filename= saveName, driver=driverSelectionInput)
