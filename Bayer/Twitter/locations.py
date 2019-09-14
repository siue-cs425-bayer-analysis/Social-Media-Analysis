#   Author: Carl Grissom
#   Date: 03/29/2019
#   File name: locations.py
#   Description: location variables for twitter geo searches. 
#       Coordinates for a city were determined by a google search    
#           "city name coordinates" i.e. Saint Louis coordinates.
#     
#       Radius is set to 100 miles from the coordinate point.
#   NOTE: When updating locations need to update LOCATIONS to reflected change      
#
#   All rights reserved.

# locations
# city = [longitude, latitude, "radius"]



LOCATIONS = {"Chicago": ("41.8781", "-87.6298", "100mi"),
             "Kansas": ("39.0997", "-94.5786", "100mi"), 
             "New York": ("40.7128", "-74.0060", "100mi"), 
             "Redmond": ("47.6740", "-122.121513", "100mi"), 
             "Los Angles": ("34.0522", "-118.2437", "100mi"), 
             "San Fransico": ("37.7749", "-122.4194", "100mi"), 
             "Saint Louis": ("38.6270", "-90.1994", "100mi") 
            }
