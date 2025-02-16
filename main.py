import phonenumbers
from phonenumbers import geocoder

# Dictionary of approximate country coordinates
country_coordinates = {
    "Iran": (32.4279, 53.6880),
    "United States": (37.0902, -95.7129),
    "Germany": (51.1657, 10.4515),
    "United Kingdom": (55.3781, -3.4360),
    "France": (46.6035, 1.8883),
    "Canada": (56.1304, -106.3468),
    "India": (20.5937, 78.9629),
    "China": (35.8617, 104.1954),
    "Japan": (36.2048, 138.2529),
    "Russia": (61.5240, 105.3188),
    # Add more countries as needed
}

def get_location_from_phone_number(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number, None)
    
    # Get the country or region
    location = geocoder.description_for_number(parsed_number, 'en')
    return location

def get_coordinates_from_country(country_name):
    # Get coordinates from the dictionary
    return country_coordinates.get(country_name, None)

def generate_google_maps_link(latitude, longitude):
    # Generate a Google Maps link
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def main():
    # Get the phone number from the user
    phone_number = input("Please enter a phone number (with country code): ")
    
    # Get the country name
    country_name = get_location_from_phone_number(phone_number)
    print(f"Country: {country_name}")
    
    # Get the country coordinates
    coordinates = get_coordinates_from_country(country_name)
    
    if coordinates:
        latitude, longitude = coordinates
        print(f"Approximate Coordinates: Latitude: {latitude}, Longitude: {longitude}")
        
        # Generate a Google Maps link
        google_maps_link = generate_google_maps_link(latitude, longitude)
        print(f"Google Maps Link: {google_maps_link}")
    else:
        print("Sorry, coordinates for this country are not available in the system.")

if __name__ == "__main__":
    main()
