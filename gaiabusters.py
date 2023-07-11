from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u


class DataTable():
    def __init__(
            self, coord, radius="2 arcsec", source_table="gaiadr3.gaia_source"):
        self.coord = coord
        # query gaia-source, get important columns
        self.source_table = source_table
        Gaia.MAIN_GAIA_TABLE = self.source_table
        self.query_result = Gaia.query_object_async(coord, radius)

    def set_source_table(source_table):
        self.source_table = source_table
        Gaia.MAIN_GAIA_TABLE = self.source_table

    def get_lightcurve(self):
        pass

    def get_spectrum(self):
        pass

    def get_sdss(self):
        pass