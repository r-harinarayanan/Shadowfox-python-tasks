# Same Country Checker (Case-Insensitive)
city1 = input("Enter the first city: ").strip().title()
city2 = input("Enter the second city: ").strip().title()

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

country1 = get_country(city1)
country2 = get_country(city2)

if country1 is None or country2 is None:
    print("One or both cities are not in the list.")
elif country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
