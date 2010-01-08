from wemd.core import ConfigError
from fixed_bins import FixedBinWEDriver

import logging
log = logging.getLogger(__name__)

def make_we_driver(sim_config):
    bin_type = sim_config['bins.type']
    if bin_type == 'fixed':
        log.info('using fixed-bin WE driver')
        driver = FixedBinWEDriver(sim_config)
    else:
        raise ConfigError('invalid bin type (%s) specified' % bin_type)
    
    return driver


        