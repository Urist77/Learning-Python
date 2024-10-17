# this program encodes and decodes a message
# review of chr() and ord()

# secret message copy pasta - What is the air speed velocity of a swallow?

def main():
    decoded = ''
    print("This program encodes and then decodes a message.")
    msg = input('Please enter your message: ')

    for character in msg:
        print(ord(character), end=' ')

    code = input('\nPlease enter your encoded message: \n')
    secret_msg = code.split()

    decoded_list = [chr(int(num))for num in secret_msg]
    print(decoded_list)
    decoded = decoded.join(decoded_list)
    print(decoded)

main()