###
#
#

import MyText

text = "An apple a day keeps the doctor away"

num_words = MyText.count_words(text)
longest_to_shortest = MyText.words_longest_to_shortest(text)
alphabetical_order = MyText.words_alphabetically(text)


print(f"Text: {text}")
print(f"Number of words: {num_words}")
print(f"Words from the longest to shortest: {', '.join(longest_to_shortest)}")
print(f"Words ordered alphabetically: {', '.join(alphabetical_order)}")
