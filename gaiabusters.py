from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u
#import numpy as np


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

    def get_epoch_photometry(self, verbose = False):

        #This is hardcoded so that this function does this one thing, should make it easier to test and validate
        retrieval_type = 'EPOCH_PHOTOMETRY'   # Options are: 'EPOCH_PHOTOMETRY', 'MCMC_GSPPHOT', 'MCMC_MSC', 'XP_SAMPLED', 'XP_CONTINUOUS', 'RVS', 'ALL'
        data_structure = 'INDIVIDUAL'   # Options are: 'INDIVIDUAL', 'COMBINED', 'RAW'
        data_release   = 'Gaia DR3'     # Options are: 'Gaia DR3' (default), 'Gaia DR2'

        datalink = Gaia.load_data(ids=self.source_table.source_id, data_release = data_release, 
                                retrieval_type=retrieval_type, 
                                data_structure = data_structure, 
                                verbose = False, output_file = None)

        dl_key = f"{retrieval_type}-{data_release} {source_id}.xml"

        if verbose:
            print(f'The following Datalink products have been downloaded:')
            
        #Convert datalink table to Astropytable and store as attribute   
        eptable = datalink[dl_key][0].to_table()  
        
        self.epoch_photometry  = dict()
        for band in ["G","BP","RP"]:
            self.epoch_photometry[band] = eptable[eptable["band"]==band]
  

    def plot_epoch_photometry(self, band = 'G', ax = None, fig = None, plot_kwargs = None):

        if fig is None: fig = plt.figure(1)
        if ax is None: ax = fig.add_subplot(111)
        tab = ep[band]
        #phase = tab["time"]/Period - np.floor(tab["time"]/Period)
        ax.plot(phase, tab["mag"], plot_kwargs)
        ax.invert_yaxis()

    def get_spectrum(self):
        pass

    def get_sdss(self):
        pass