import argparse
import math
import re
import sys

"""
This script calculates a supernet prefix sufficient to contain a supplied list of subnet prefixes.
This accounts for growth in the network, setting a default growth to 40%.
Example invocation:  python .\addsubnets.py /24 /24 /23 /22
Output: /20
Author: Jodie Cunningham
Date: October 19, 2023
"""

def calculate_subnet(cidr_list, extra_percentage=40):
    addresses_required = 0

    for cidr in cidr_list:
        if not re.match(r'/\d{1,2}', cidr) or int(cidr[1:]) > 32:
            print(f"Invalid CIDR range: {cidr}")
            sys.exit(1)
        addresses_required += 2 ** (32 - int(cidr[1:]))

    addresses_required += (addresses_required * extra_percentage) / 100
    prefix_length = 32 - math.ceil(math.log2(addresses_required))

    return f"/{prefix_length}"

def main():
    parser = argparse.ArgumentParser(description="Calculate a supernet prefix to contain a list of subnet prefixes.")
    
    parser.add_argument('cidr_list', metavar='CIDR', nargs='+', help='List of subnet prefixes in CIDR notation')
    parser.add_argument('-e', '--extra', type=int, default=40, help='Percentage of extra growth (default: 40)')
    
    args = parser.parse_args()
    
    if args.extra < 0 or args.extra > 500:
        print("Extra percentage must be between 0 and 500.")
        sys.exit(1)

    result = calculate_subnet(args.cidr_list, args.extra)
    print(result)

if __name__ == "__main__":
    main()
