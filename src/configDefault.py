""" Actual configurations used by the project.
    DO NOT MODIFY, 
    instead modify values in configLocal.py """

from configLocal import config as configLocal

config = {
    'radarRootPath': '',
    'satelliteRootPath': '',
    'gmapsKey': ''
}

# override common keys from local config
for k, v in configLocal.items():
    if k in config:
        config[k] = v

import os
cached_listdir_sat = os.listdir(config['satelliteRootPath'])
