def print_upper_words(words,must_start_with):
    """For a list of words, print out
    each word on a separate line. All
    words will be printed in uppercase.
    must_start_with is a passed in set of letters.
    If word starts with any letter from set,
    then the caps version will be printed.
    
    For example: 
        print_upper_words(["hello","hey","bye"],{"h"})
    
    Should print:
        HELLO, HEY

    For example: 
        print_upper_words(["hello","hey","bye"],{"h","y"})
    
    Should print:
        HELLO, HEY, YO, YES
    """

    # MY CODE
    new_words = []
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                word = word.upper()
                new_words.append(word)
    return print(", ".join(new_words))
