###
#
#

def count_words(text):      # Count the number of words in text
    words = text.split()    # Split text into words at spaces
    return len(words)       # Number of worsd


def words_longest_to_shortest(text):    # Return words in order from long to short
    words = text.split()                # Split text
    words_sorted = sorted(words, key=len, reverse=True)  # Sort words by length (longest first)
    return words_sorted


def words_alphabetically(text):     # Return the words ordered alphabetically
    words = text.split()            # Split text
    words_ordered = sorted(words)   # Sort words alphabetically
    return words_ordered
