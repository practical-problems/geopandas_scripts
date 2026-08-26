import geopandas
from pathlib import Path

class GeoFile:
    def __init__(self, file_location : str):
        self.fileLocation = file_location
        self.loadStatus = False
        self.gdf = None

    def load(self):
        self.gdf = geopandas.read_file(self.fileLocation)
        self.loadStatus = True

    def save(self, save_file_name : str, save_file_type : str):
        if not self.loadStatus:
            raise ValueError("There no file loaded in memory")
        self.gdf.to_file(filename = save_file_name, driver = save_file_type)

    def set_crs(self, projection_to_be_set_to : str):
        if not self.loadStatus:
            raise ValueError("You must call .load() before setting a projection.")
        if self.gdf.crs is not None:
            raise ValueError("There already an projection in " + str(self.fileLocation))
        self.gdf = self.gdf.set_crs(projection_to_be_set_to)

    def reproject(self, projection_to_be_set_to : str):
        if not self.loadStatus:
            raise ValueError("You must call .load() before changing the projection.")
        if self.gdf.crs is None:
            raise ValueError("There is no projections in the file!")
        self.gdf = self.gdf.to_crs(projection_to_be_set_to)


def init_geo_folder(folder_directory : str, file_type: str = ".shp", recursive : bool = False) -> tuple[
    dict[str, GeoFile], dict[str, str]]: #it is not recursive by default
    folder = Path(folder_directory)
    errors = {}
    output : dict[str, GeoFile] = {}
    glob_status = "*"
    if recursive:
        glob_status = "**/*"
    for file in folder.glob(glob_status+file_type): #find the file and create new GeoFile class
        try:
            if file_type == ".shp":
                if not file.with_suffix(".dbf").exists():
                    raise ValueError(f"{file.name}: missing .dbf file")
                if not file.with_suffix(".shx").exists():
                    raise ValueError(f"{file.name}: missing .shx file")
            file_object =  GeoFile(str(file.resolve()))
            output[file.name] = file_object
        except ValueError as error_string:
            errors[file.name] = str(error_string)
    return output, errors

