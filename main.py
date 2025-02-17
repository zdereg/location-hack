import phonenumbers
from phonenumbers import geocoder

# Dictionary of approximate city coordinates in Iran
iran_city_coordinates = {
    "021": (35.6892, 51.3890),  # Tehran
    "026": (35.7000, 51.3667),  # Karaj
    "031": (32.6539, 51.6660),  # Isfahan
    "0314": (32.5055, 51.6938),  # Fooladshahr
    "0314": (32.5550, 51.5097),  # Falavarjan
    "044": (37.2761, 49.5886),  # Rasht
    "051": (36.2605, 59.6168),  # Mashhad
    "056": (33.8589, 48.8296),  # Khorramabad
    "061": (31.3183, 48.6706),  # Ahvaz
    "024": (34.3418, 47.0755),  # Kermanshah
    "074": (30.2839, 57.0834),  # Kerman
    "071": (29.5926, 52.5836),  # Shiraz
    "054": (36.5633, 53.0601),  # Sari
    "011": (37.2808, 49.5832),  # Bandar Anzali
    "017": (36.5633, 53.0601),  # Nowshahr
    "041": (38.0800, 46.2919),  # Tabriz
    "087": (34.3142, 47.0650),  # Hamedan
    "058": (37.5527, 45.0759),  # Urmia
    "083": (34.7989, 48.5150),  # Malayer
    "081": (34.0925, 49.6984),  # Arak
    "086": (33.8964, 48.7516),  # Borujerd
    "025": (36.4696, 52.3507),  # Qaemshahr
    "023": (35.2972, 52.5075),  # Damghan
    "045": (37.0667, 54.1667),  # Gorgan
    "0512": (36.2605, 59.6168),  # Mashhad (old area code)
    "0513": (36.2605, 59.6168),  # Mashhad (old area code)
}

# Dictionary of streets in Fooladshahr
fooladshahr_streets = {
    "Imam Khomeini Street": (32.5055, 51.6938),
    "Enghelab Street": (32.5060, 51.6940),
    "Shahid Motahari Street": (32.5070, 51.6950),
    "Azadi Street": (32.5080, 51.6960),
    "Shariati Street": (32.5090, 51.6970),
    "Ghods Street": (32.5100, 51.6980),
    "Beheshti Street": (32.5110, 51.6990),
    "Zeynabieh Street": (32.5120, 51.7000),
    "Shahid Rajaei Street": (32.5130, 51.7010),
    "Shahid Beheshti Street": (32.5140, 51.7020),
    # Add more streets as needed
}

# Dictionary of approximate country coordinates
country_coordinates = {
    "Iran": (32.4279, 53.6880),
    "United States": (37.0902, -95.7129),
    "Germany": (51.1657, 10.4515),
    # Add more countries as needed
}

def get_location_from_phone_number(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number, None)
    
    # Get the country or region
    location = geocoder.description_for_number(parsed_number, 'en')
    return location

def get_city_from_phone_number(phone_number):
    # Check if the number is the specific mobile number
    if phone_number == "+989940604817":
        return "Fooladshahr", (32.5055, 51.6938)
    
    # Extract the area code (assuming the number is in international format)
    if phone_number.startswith("+98"):
        area_code = phone_number[3:6]  # Extract the first three digits after +98
        return iran_city_coordinates.get(area_code, None)
    return None

def get_coordinates_from_country(country_name):
    # Get coordinates from the dictionary
    return country_coordinates.get(country_name, None)

def generate_google_maps_link(latitude, longitude):
    # Generate a Google Maps link
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def main():
    # Get the phone number from the user
    phone_number = input("Please enter a phone number with the country code: ")
    
    # Get the country name
    country_name = get_location_from_phone_number(phone_number)
    print(f"Country: {country_name}")
    
    if country_name == "Iran":
        # Try to get the city coordinates
        city_info = get_city_from_phone_number(phone_number)
        if city_info:
            city_name, (latitude, longitude) = city_info
            print(f"City: {city_name}")
            print(f"Approximate City Coordinates: Latitude: {latitude}, Longitude: {longitude}")
            
            # Generate a Google Maps link
            google_maps_link = generate_google_maps_link(latitude, longitude)
            print(f"Google Maps Link: {google_maps_link}")
            
            # Check if the city is Fooladshahr
            if city_name == "Fooladshahr":
                print("\nStreets in Fooladshahr:")
                for street, (lat, lon) in fooladshahr_streets.items():
                    print(f"{street}: Latitude: {lat}, Longitude: {lon}")
        else:
            print("Sorry, coordinates for this city are not available in the system.")
    else:
        # Get the country coordinates
        coordinates = get_coordinates_from_country(country_name)
        if coordinates:
            latitude, longitude = coordinates
            print(f"Approximate Country Coordinates: Latitude: {latitude}, Longitude: {longitude}")
            
            # Generate a Google Maps link
            google_maps_link = generate_google_maps_link(latitude, longitude)
            print(f"Google Maps Link: {google_maps_link}")
        else:
            print("Sorry, coordinates for this country are not available in the system.")

if __name__ == "__main__":
    main()
