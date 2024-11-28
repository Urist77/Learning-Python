
def main():
    mailbox_directory = {'Mel': 'H344', 'Gil': 'G177', 'Mai': 'G830', 'Ari': 'E584'}
    amount_of_mail = {'H344': 8, 'G177': 14, 'G830': 16, 'E584': 7}

    resident_name = input()

    mailbox_code = mailbox_directory.get(resident_name, 'no info')
    num_mail = amount_of_mail.pop(mailbox_code, -9)

    print(f'{resident_name} (mailbox {mailbox_code}) picked up {num_mail} letters.')
    print('Remaining mail:')
    print(amount_of_mail)

main()