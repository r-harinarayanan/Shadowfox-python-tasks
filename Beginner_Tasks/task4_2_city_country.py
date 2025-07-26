# City to Country Checker (Case-Insensitive)
city = input("Enter a city name: ").strip().title()

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list")
