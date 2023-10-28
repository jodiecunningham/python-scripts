import argparse
import random
import string

# Generate a random string for SSID that meets the following constraints:  
# The printable characters plus the space (ASCII 0x20) are allowed, but these six characters are not: ?, ", $, [, \, ], and +
# Default length parameter is 16 characters, maximum is 32 per the IEEE 802.11 spec

def genSSID(length=16):
    disallowed_chars = set('?"$[\\]+')
    allowed_chars = ''.join(c for c in string.printable[:-6] if c not in disallowed_chars)
    return ''.join(random.choice(allowed_chars) for i in range(length))

def main(): 
    parser = argparse.ArgumentParser(description='Generate a random SSID.')
    parser.add_argument('-l', '--length', type=int, default=16, help='Length of the SSID')

    args = parser.parse_args()
    length = args.length

    if length < 2 or length > 32:
        print("Length must be between 2 and 32.")
        parser.print_usage()
        return

    random_string = genSSID(length)
    print(f"Generated SSID: {random_string}")

if __name__ == "__main__":
    main()    