airports = {}
def enter_airport():
    icao_code = input("Enter the ICAO code: ").strip().upper()
    airport_name = input("Enter the airport name: ").strip()
    if icao_code and airport_name:
        airports[icao_code] = airport_name
        print(f"Airport '{airport_name}' with ICAO code '{icao_code}' has been updated.")
    else:
        print("Invalid input.")
def fetch_airport():
    icao_code = input("Enter the ICAO code: ").strip().upper()
    if icao_code in airports:
        print(f"The airport name for ICAO code '{icao_code}' is: {airports[icao_code]}")
    else:
        print(f"Airport with ICAO code '{icao_code}' not EXISTING.")
def main():
    while True:
        print("\nAirport Information:")
        print("1. Enter a new airport")
        print("2. Fetch information")
        print("3. Quit the program")
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice == '1':
            enter_airport()
        elif choice == '2':
            fetch_airport()
        elif choice == '3':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()