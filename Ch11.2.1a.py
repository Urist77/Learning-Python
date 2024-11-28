# Introduction of .get() and .pop() method
# Both methods are safe if the key is not in the dictionary
# Printing by a key or deleting by a key will not work if the key is not in the dictionary

def main():
    ap_codes = {
        'Paris': 'CDG',
        'Dallas': 'DAL', # DFW
        'Osaka': 'KIX',
        'Washington': 'IAD',
        'Seattle': 'SEA'
    }

    ap_codes['Dallas'] = 'DFW' # approach to change the value
    ap_codes['Tulsa'] = 'TUL' # or add a new key:value pair
    print(ap_codes)

    if 'Dallas' in ap_codes:
        print(f'{ap_codes['Dallas']}')
    else:
        print('Dallas is not there.')

    print(ap_codes.get('Dallas', 'That is not in the dictionary')) # .get(key, error message) format
    print(ap_codes.get('Houston', 'That is not in the dictionary'))
    # The .get() method is safe even of a key is not in the dictionary
    print(ap_codes.pop('Dallas', 'That is not in the dictionary'))
    print(ap_codes.pop('Dallas', 'That is not in the dictionary'))

main()