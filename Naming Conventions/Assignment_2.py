# Create a console application that takes the input as a Country Code (Eg: IN/US/NZ ) and gives the adjacent Country's names (In Full). 
def get_country_name_from_code(country_code):
    country_codes = {
        "IN": "India",
        "US": "United States",
        "NZ": "New Zealand",
        "CN": "China",
        "PK": "Pakistan",
        "BD": "Bangladesh",
        "CA": "Canada",
        "MX": "Mexico",
        "AU": "Australia",
        "FJ": "Fiji"
    }
    return country_codes.get(country_code.upper(), None)

def get_adjacent_countries(country_code):
    adjacency_list = {
        "IN": ["CN", "PK", "BD"],
        "US": ["CA", "MX"],
        "NZ": ["AU", "FJ"],
        "CN": ["IN", "PK"],
        "PK": ["IN", "CN"],
        "BD": ["IN"],
        "CA": ["US"],
        "MX": ["US"],
        "AU": ["NZ", "FJ"],
        "FJ": ["NZ", "AU"]
    }
    return adjacency_list.get(country_code.upper(), [])

def main():
    print("Country Adjacency Finder")
    country_code = input("Enter the country code (e.g., IN, US, NZ): ").strip()

    # Get the full country name
    country_name = get_country_name_from_code(country_code)
    if not country_name:
        print(f"Invalid country code: {country_code}")
        return

    # Get the adjacent countries
    adjacent_codes = get_adjacent_countries(country_code)
    if not adjacent_codes:
        print(f"No adjacency information available for {country_name}.")
        return

    # Convert codes to full names
    adjacent_countries = [get_country_name_from_code(code) for code in adjacent_codes]
    print(f"Adjacent countries to {country_name} ({country_code.upper()}):")
    for country in adjacent_countries:
        print(f"- {country}")

if __name__ == "__main__":
    main()