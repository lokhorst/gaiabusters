from astropy.coordinates import SkyCoord
import astropy.units as u
from gaiabusters import DataTable


def test_query_result():
    c = SkyCoord(ra="280 deg", dec="-60 deg", frame='icrs')
    x = DataTable(c, radius="2 arcmin")
    assert len(x.query_result) > 0, "Empty table returned."