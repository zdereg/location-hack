while True:
    import requests
    def get_ip_info(ip):
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()
        return data

    def generate_google_maps_link(latitude, longitude):
        return f"https://www.google.com/maps?q={latitude},{longitude}"

    ip = input("Enter IP address: ")
    info = get_ip_info(ip)
    print("\nIP Information:")
    print(f"IP: {info.get('ip')}")
    print(f"City: {info.get('city')}")
    print(f"Region: {info.get('region')}")
    print(f"Country: {info.get('country')}")
    print(f"ISP: {info.get('org')}")

    if 'loc' in info:
        latitude, longitude = info['loc'].split(',')
        google_maps_link = generate_google_maps_link(latitude, longitude)
        print(f"\nGoogle Maps Link: {google_maps_link}")
    else:
            print("\nLocation data not available for this IP.")
