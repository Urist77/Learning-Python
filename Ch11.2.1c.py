# joining two dictionaries together


def main():
    ap_codes = {
        'Paris': 'CDG',
        'Dallas': 'DAL', # DFW
        'Osaka': 'KIX',
        'Washington': 'IAD',
        'Seattle': 'SEA'
    }

    new_ap_codes = {
        'Dallas': 'DFW', # keys must be unique
        'Tulsa': 'TUL',
        'Bozeman': 'BZN'
    }

    print(f'original ap_codes: {ap_codes}')
    ap_codes.update(new_ap_codes)
    print(new_ap_codes)
    print(f'updated ap_codes: {ap_codes}')

main()