# gaiabusters

[![Go to Code/Astro website](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)


### Query the Gaia archive for light curves and SDSS images.

"Let's make a package to query Gaia and other data!"  
"What are we gonna call it?"  
"Ghostbusters!"  
"..."  
"Gaiabusters?"  
"YES!"


## Example Use
```
import gaiabusters as gb
from astropy.coordinates import SkyCoord

# Input coordinates and radius for cone search
c = SkyCoord('0h8m05.63s +14d50m23.3s', frame='icrs')
dt = gb.DataTable(c, radius="10 arcsec")
print(dt.source_id)

# get SDSS data and plot
res = dt.get_sdss()

dt.plot_sdss()
```