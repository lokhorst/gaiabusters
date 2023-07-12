from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np


class DataTable():
    def __init__(self, coord, radius="10 arcsec", source_table="gaiadr3.gaia_source"):
        """ Initialize DataTable object to hold GAIA data information (+ other sources).
        Currently finds closest source to specified coordinates.

        Args:
            coord (SkyCoord): Coordinates of the target/field
            radius (str, optional): Search radius including units. Defaults to "10 arcsec".
            source_table (str, optional): Which gaia source table to query. Can specify dr2, dr3, etc.
                Needs to be a source table. Defaults to "gaiadr3.gaia_source".
        """
        
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
        """Setting the source table variables with search output.
        (to do: have a list of available source tables and assert that
        specified table is in the list before continuing - display available
        source tables)

        Args:
            source_table (str): Name of the source table to be searched.
        """
        self.source_table = source_table
        Gaia.MAIN_GAIA_TABLE = self.source_table

    def get_epoch_photometry(self, verbose = False):
        """ Retrieves epoch photometry data from datalink for current object.

        Args:
            verbose (bool, optional): Prints verbose statements. Defaults to False.
        """

        #This is hardcoded so that this function does this one thing, should make it easier to test and validate
        retrieval_type = 'EPOCH_PHOTOMETRY'   # Options are: 'EPOCH_PHOTOMETRY', 'MCMC_GSPPHOT', 'MCMC_MSC', 'XP_SAMPLED', 'XP_CONTINUOUS', 'RVS', 'ALL'
        data_structure = 'INDIVIDUAL'   # Options are: 'INDIVIDUAL', 'COMBINED', 'RAW'
        data_release   = 'Gaia DR3'     # Options are: 'Gaia DR3' (default), 'Gaia DR2'

        assert np.ndim(self.source_id)==0, "Check that source id is scalar, just in case" 
        assert int(self.source_id), "Wrong type: source_id cannot be converted to int (needed by astroquery)"

        #int is necessary for astroquery to work, it doesn't like np.int64 
        datalink = Gaia.load_data(ids=int(self.source_id), data_release = data_release, 
                                retrieval_type=retrieval_type, 
                                data_structure = data_structure, 
                                verbose = False, output_file = None)

        dl_key = f"{retrieval_type}-{data_release} {self.source_id}.xml"

        if verbose:
            print(f'Datalink {retrieval_type} retrieved from {data_release}')
            
        #Convert datalink table to Astropytable and store as attribute   
        eptable = datalink[dl_key][0].to_table()  
        
        self.epoch_photometry  = dict()
        for band in ["G","BP","RP"]:
            self.epoch_photometry[band] = eptable[eptable["band"]==band]
  

    def plot_epoch_photometry(self, band = 'G', ax = None, fig = None, plot_kwargs = None):

        pass
        # if fig is None: fig = plt.figure(1)
        # if ax is None: ax = fig.add_subplot(111)
        # tab = ep[band]
        # #phase = tab["time"]/Period - np.floor(tab["time"]/Period)
        # ax.plot(phase, tab["mag"], plot_kwargs)
        # ax.invert_yaxis()

    def get_spectrum(self):
        pass

    def get_sdss(self):
        pass