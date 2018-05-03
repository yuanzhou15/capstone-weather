""" Actual configurations used by the project.
    DO NOT MODIFY, 
    instead modify values in configLocal.py """

from .configLocal import config as configLocal

config = {
    'radarRootPath': '/home/yuan/Documents/Spring-2018/Senior Design/Weather/new-radar-data',
    'satelliteRootPath': '/home/yuan/Documents/Spring-2018/Senior Design/Weather/Satellite-data',
    'gmapsKey': ''  # googlemaps api key, used for any maps-related code using gmaps library
}

# override common keys from local config
for k, v in configLocal.items():
    if k in config:
        config[k] = v

# files in satelliteRootPath are enumerated a lot, so we'll cache them here
import os
cached_listdir_sat = os.listdir(config['satelliteRootPath'])
