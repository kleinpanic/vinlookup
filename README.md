# VIN Lookup Tool

This is a simple Python script that retrieves vehicle information based on a VIN (Vehicle Identification Number) using the [NHTSA API](https://vpic.nhtsa.dot.gov/api/).

## Features
- Fetches vehicle details by VIN.
- Uses the NHTSA public API for VIN decoding.
- Simple command-line interface.

## Requirements
This script requires Python 3 and the `requests` library.

Install the required dependency using (if you don't have it by default):
```sh
pip install requests
```

## Usage
Run the script and enter a VIN when prompted:
```sh
python vin_lookup.py
```
Then input the VIN to retrieve details about the vehicle.

## Example Output
```
Enter the VIN: 1HGCM82633A123456
Vehicle Info:
Make: Honda
Model: Accord
Model Year: 2003
Body Class: Sedan/Saloon
...
```

## Project Structure
```
.
├── vin_lookup.py   # Main script
├── README.md       # Project documentation
├── LICENSE         # MIT License
```

## API Information
This script utilizes the [NHTSA Vehicle API](https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/) to retrieve vehicle details.

## License
This project is licensed under the MIT License.
