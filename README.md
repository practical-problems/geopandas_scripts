//GeoFile Utilities

A lightweight Python utility for batch loading, reprojecting, and saving geospatial vector files using GeoPandas.

//Features
Load and save vector files (Shapefile, GeoJSON, etc.) through a simple class interface
Set or reproject coordinate reference systems (CRS)
Batch-initialize entire folders of geospatial files with built-in error handling
Validates Shapefile component files (.dbf, .shx) before loading
Supports recursive directory traversal
//Requirements
Python 3.10+
GeoPandas

//Notes
.load() must be called before any projection or save operations
set_crs() is for assigning a CRS to files that have none; use reproject() to convert between projections
init_geo_folder() returns a tuple of successfully initialized files and a dict of errors keyed by filename
