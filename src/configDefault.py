""" Actual configurations used by the project. """

from os import environ

if not 'weatherdata' in environ:
    Exception("Environment Varaiable 'weather' does not exist")
weatherdata = environ['weather']
if weatherdata[-1] not in ['/', '\\']:
    weatherdata += '/'

config = {
    'radarRootPath': weatherdata + 'radar/',
    'satelliteRootPath': weatherdata + 'satellite/',
    'gmapsKey': ''  # googlemaps api key, used for any maps-related code using gmaps library
}

# files in satelliteRootPath are enumerated a lot, so we'll cache them here
import os
cached_listdir_sat = os.listdir(config['satelliteRootPath'])
