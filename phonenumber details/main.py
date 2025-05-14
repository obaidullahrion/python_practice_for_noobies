import phonenumbers
from phonenumbers import carrier , geocoder , timezone
import requests
mobileNO = input("target number : ")
mobileNO = phonenumbers.parse(mobileNO)

print(timezone.time_zones_for_number(mobileNO))
print(carrier.name_for_number(mobileNO , "en"))
print(geocoder.description_for_number(mobileNO, "en"))
print("valid Mobile Number :" , phonenumbers.is_valid_number(mobileNO))
print("checking possiblity of number :"  , phonenumbers.is_possible_number(mobileNO))

