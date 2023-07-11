from astropy.coordinates import SkyCoord
import astropy.units as u
from gaiabusters import DataTable


def test_query_result():
    c = SkyCoord(ra="18 36 56.33", dec="+38 47 01.28", frame="icrs", 
        unit=(u.hourangle, u.deg), obstime="J2000")
    x = DataTable(c, radius="2 arcmin")
    assert len(x.query_result) > 0, "Empty table returned."