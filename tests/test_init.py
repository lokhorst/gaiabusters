from astropy.coordinates import SkyCoord
from astropy.io import fits
from gaiabusters import DataTable
import numpy as np

def test_query_result():
    c = SkyCoord(ra="280 deg", dec="-60 deg", frame='icrs')
    x = DataTable(c, radius="2 arcmin")
    assert len(x.query_result) > 0, "Empty table returned."
    
def test_SDSS_query_result_and_plotting():
    """Testing the get_sdss functionality.
    This should populated the sdss_im variable
    with an hdu object containing data and header info.
    After successful query, the plotting functionality is tested.
    """
    c = SkyCoord('0h8m05.63s +14d50m23.3s', frame='icrs')
    radius="10 arcsec"
    x = DataTable(c, radius=radius)
    
    res = x.get_sdss()
    
    assert res is not None, "Coordinates out of range for SDSS?"
    assert isinstance(x.sdss_im.data,np.ndarray)
    assert isinstance(x.sdss_im.header,fits.header.Header)
    assert x.sdss_im.data.shape[0]>0, "Returned an empty or wrong format data array"
    assert x.sdss_im.data.shape[1]>0, "Returned an empty or wrong format data array"

    x.plot_sdss()
    
    # hdu = fits.PrimaryHDU(array,header=wcs_out.to_header())
    # hdu.writeto(f'mosaic.fits',overwrite=True)
