# Chapter 12 - The Country Code Program

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()

    for code in codes:
        print(code, countries[code])


def main():
    countries = {
        "CA": "Canada",
        "US": "United States",
        "MX": "Mexico"
    }

    print("Country Codes")
    display_codes(countries)

    code = input("\nEnter a country code: ")
    code = code.upper()

    if code in countries:
        print("Country:", countries[code])
    else:
        print("There is no country with that code.")


if __name__ == "__main__":
    main()
