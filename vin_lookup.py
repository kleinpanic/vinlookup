import requests

def get_vehicle_info_by_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['Results']:
            return data['Results']
        else:
            return {"error": "No results found"}
    else:
        return {"Error": f"Request failed. Status code: {response.status_code}"}
def main():
    vin = input("Enter the VIN: ").strip()
    vehicle_info = get_vehicle_info_by_vin(vin)

    if "error" not in vehicle_info:
        print("Vehicle Info:")
        for item in vehicle_info:
            if item['Variable'] and item['Value']:
                print(f"{item['Variable']}:{item['Value']}")
    else:
        print(vehicle_info['error'])

if __name__ == "__main__":
    main()

