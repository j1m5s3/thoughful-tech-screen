import argparse
import json
from typing import Literal

BULKY_MAX = 1000000.0  # cubic cm
DIMENSION_LIMIT = 150.0  # cm
MASS_MAX = 20.0  # kg

def sort(width: float, height: float, length:float, mass: float) -> Literal['STANDARD', 'SPECIAL', 'REJECTED']:
    """
    Classify a package based on its dimensions and mass.

    A package is BULKY if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
    or when one of its dimensions is greater or equal to 150 cm

    A package is HEAVY when its mass is greater or equal to 20 kg.

    The classification rules are as follows:
    STANDARD: standard packages (those that are not BULKY or HEAVY) can be handled normally
    SPECIAL: packages that are either HEAVY or BULKY can't be handled automatically
    REJECTED: packages that are both HEAVY and BULKY are rejected

    :param width: Width in cm
    :param height: Height in cm
    :param length: Length in cm
    :param mass: Mass in kg

    :return: Package classification as 'STANDARD', 'SPECIAL', or 'REJECTED'
    """
    # Create an assert that ensures all dimensions and mass are positive numbers
    assert all(dim > 0 for dim in [width, height, length, mass]), "All dimensions and mass must be positive numbers"
    # Create an assert that all dimensions and mass are of type float
    assert all(isinstance(dim, (int, float)) for dim in [width, height, length, mass]), "All dimensions and mass must be numbers"
    volume: float = width * height * length

    # Use any to check if any dimension exceeds 150 cm
    bulk_dimension_check: bool = any(dim > DIMENSION_LIMIT for dim in [width, height, length])
    vol_gte_max: bool = volume >= BULKY_MAX

    bulky: bool = bulk_dimension_check or vol_gte_max
    heavy: bool = mass >= MASS_MAX
    rejected: bool = bulky and heavy
    standard: bool = not bulky and not heavy

    if bulky or heavy:
        if rejected:
            return 'REJECTED'
        else:
            return 'SPECIAL'
    elif standard:
        return 'STANDARD'
    else:
        raise Exception("Unable to classify package")



if __name__ == "__main__":
    # Add the ability to pass a file path to a json file that contains the dimensions and mass
    parser = argparse.ArgumentParser(description='Package Sorter')
    parser.add_argument(
        "--file", type=str, help="Path to json file containing package dimensions and mass"
    )
    args = parser.parse_args()

    if args.file is None:
        with open('./test_data.json', 'r') as f:
            data = json.load(f)
    else:
        with open(args.file, 'r') as f:
            data = json.load(f)

    test_results = {}
    for key in data.keys():
        input_width = float(data[key]['width'])
        input_height = float(data[key]['height'])
        input_length = float(data[key]['length'])
        input_mass = float(data[key]['mass'])
        classification = sort(
            width=input_width,
            height=input_height,
            length=input_length,
            mass=input_mass
        )
        print(f"Package classification({key}): {classification}")
        test_results[key] = classification

    with(open('test_results.json', 'w') as f):
        json.dump(test_results, f, indent=4)

