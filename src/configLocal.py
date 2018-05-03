""" Use this to override defualt project settings, 
    or set configs specific to you local repo/machine,
    like paths to files or credentials.
    This should only ever be used/imported in configDefault and nowhere else """

# uncomment to override. None or '' values will still cause an override!!
config = {
    'radarRootPath': '/home/yuan/Documents/Spring-2018/Senior Design/Weather/test-radar',
    'satelliteRootPath': '/home/yuan/Documents/Spring-2018/Senior Design/Weather/test-satellite',
    'gmapsKey': ''  # googlemaps api key, used for any maps-related code using gmaps library
}
