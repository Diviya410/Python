# track location and time zone using the phone number
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

import folium
from opencage.geocoder import OpenCageGeocode

 
number = input("Enter the phone number with country code : ")
 
# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)

# Key = " Enter your Api"
Key = "2278135bc03d4512873cb6a75abf35d4"

# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+geolocation)
 
# printing the timezone using the timezone module
timeZone = timezone.time_zones_for_number(phoneNumber)
print("timezone : "+str(timeZone))

# printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+service)
 
# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(geolocation)
results = geocoder.geocode(query)
 
# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
 
# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)
 
# Adding a Marker on the map to show the location name
folium.Marker([lat,lng],popup=geolocation).add_to(myMap)
 
# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")

