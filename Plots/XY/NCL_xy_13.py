"""
NCL_xy_12.py
===============
This script illustrates the following concepts:
   - Adding error bars on an XY plot

See following URLs to see the reproduced NCL plot & script:
    - Original NCL script: https://www.ncl.ucar.edu/Applications/Scripts/xy_13.ncl
    - Original NCL plots: https://www.ncl.ucar.edu/Applications/Images/xy_13_lg.png
"""

##############################################################################
# Import packages:
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

import geocat.datafiles as gdf
from geocat.viz import util as gvutil

##############################################################################
# Read in data:

# Open a netCDF data file using xarray default engine and load the data into
# xarrays
ds = xr.open_dataset(gdf.get("netcdf_files/uv300.nc"))

# Extract data
V = ds.isel(time=0, lat=30, drop=True).V

##############################################################################
# Method 1: Splitting the line into parts and coloring them differently
plt.figure(figsize=(8, 8))
ax = plt.axes()

# Use geocat.viz.util convenience function to set axes parameters
gvutil.set_axes_limits_and_ticks(ax,
                                 xlim=(0, 70),
                                 ylim=(-9, 9),
                                 xticks=np.arange(0, 71, 10),
                                 yticks=np.arange(-9, 10, 3),
                                 yticklabels=np.arange(-9.0, 10.0, 3.0))

# Use geocat.viz.util convenience function to add minor and major tick lines
gvutil.add_major_minor_ticks(ax,
                             x_minor_per_major=5,
                             y_minor_per_major=3,
                             labelsize=14)

# Use geocat.viz.util convenience function to set titles and labels
gvutil.set_titles_and_labels(ax,
                             maintitle="Example of error bars",
                             ylabel=V.long_name + " " + V.units)

plt.show()
