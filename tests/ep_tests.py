#from gaiabusters import DataTable
import init_tests
import astropy.io.ascii
import astropy.coordinates as ac
import astropy.units as u
import gaiabusters
import numpy as np

#This only works for DR3 as source_ids change with DRs
def test_get_epoch_photometry(source_id=245002531050576896):
    #For DR3: 245002531050576896 ra=57.4520443888418*u.deg, dec=46.14083266949593*u.deg is an RR Lyrae
    rrcoo = ac.SkyCoord(ra=57.4520443888418*u.deg, dec=46.14083266949593*u.deg, frame='icrs')

    dt = gaiabusters.DataTable(rrcoo)
    #Check the source id matches
    assert dt.source_id == 245002531050576896, 'ERROR: Mismatching source_id. Control object set up for Gaia DR3'

    #Get epoch photometry for our lovely object
    print('Getting epoch photometry...')
    dt.get_epoch_photometry(verbose = True)

    #BP/RP can be empty, G cannot, so only test that
    assert len(dt.epoch_photometry['G']) > 0, "ERROR: Empty table returned (G-band)"

    #Read in control table
    control_tb = astropy.io.ascii.read('ep_testdata.csv',format='csv')
    control = {}
    for band in ["G","BP","RP"]:
        control[band] = control_tb[control_tb['band']==band]

    for band in ["G","BP","RP"]:
        #Check that all keywords in control table are the same
        assert control[band].keys() == dt.epoch_photometry[band].keys(), "ERROR: the keys of epoch_photometry table don't match the control table"
        #Check the values in the table match
        assert np.allclose(control[band]['mag'], dt.epoch_photometry[band]['mag']), 'Nope...'

    print(' Epoch_Photometry Tests passed... (Yay!)')

init_tests.test_query_result()

test_get_epoch_photometry()