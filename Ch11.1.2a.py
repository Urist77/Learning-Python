# Review of dictionaries

def main():
    ap_codes = {
        'Paris': 'CDG',
        'Dallas': 'DAL',
        'Osaka': 'KIX'
    }
    print(f'{ap_codes['Dallas']}')
    ap_codes['Dallas'] = 'DFW'
    print(ap_codes['Dallas'])
    print(ap_codes['Osaka'])

main()