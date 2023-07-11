from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u


class DataTable():
    def __init__(self, coord, radius="10 arcsec", source_table="gaiadr3.gaia_source"):
        self.coord = coord
        # configure Gaia query environment
        self.set_source_table(source_table)
        Gaia.ROW_LIMIT = 1
        # query gaia-source, ensure we get a row
        self.query_result = Gaia.query_object_async(coord, radius)
        assert len(self.query_result) > 0, "Empty table returned."
        # set source ID
        self.source_id = self.query_result[0]["source_id"]

    def set_source_table(self, source_table):
        self.source_table = source_table
        Gaia.MAIN_GAIA_TABLE = self.source_table

    def get_lightcurve(self):
        pass

    def get_spectrum(self):
        pass

    def get_sdss(self):
        pass