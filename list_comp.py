# intro to list comprehension
# application of the len() function, .upper(), .lower() methods to strings

def main():
    # string = 'The quick brown fox jumps over the lazy dog.'
    # word_list = string.split()
    word_list = 'The quick brown fox jumps over the lazy dog.'.split()
    print(word_list)
    new_word_list = [[len(word), word.upper(),word.lower()] for word in word_list]
    print(new_word_list)
    for lst in new_word_list:
        print(lst)

main()