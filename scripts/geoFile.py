import geopandas


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

    def set_projection(self, projection_to_be_set_to : str):
        if self.gdf.crs is not None:
            raise ValueError("There already an projection in " + str(self.fileLocation))
        self.gdf = self.gdf.set_crs(projection_to_be_set_to)

    def reproject(self, projection_to_be_set_to : str):
        if self.gdf.crs is None:
            raise ValueError("There is no projections in the file!")
        self.gdf = self.gdf.to_crs(projection_to_be_set_to)
