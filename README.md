# pyre
PyRe is a python implementation of regex. Its main aim is to be easy to use and readable. (This is only a hobby project and is a work in progress)

Examples:

from pyre import Text

text = Text('The 6 quick brown foxes jump over 12 lazy dogs 123 times! The ducks quack braveley as the hunter takes his aim.')

text.starts_with('Th')
# >> ['The']

text.ends_with('dogs')
# >> []

text.contains('The')
# >> ['The', 'The']

# This is a special case function that returns a dict of the indexes that the matched sequence begins with
text.contains_d('The')
# >> {'The': [0, 58]}

# Get characters in text from lowercase n to uppercase T (regex: [n-zA-T])
characters = text.get_characters('n', 'T')
# >> ['T', 'q', 'u', 'r', 'o', 'w', 'n', 'o', 'x', 'u', 'p', 's', 'o', 'v', 'r', 't', 'z', 'y', 'o']

# Get digits
digits = text.get_digits()
# >> ['6', '1', '2', '1', '2', '3']

# Find any sequence that matches the following: start dequence, amount of characters in between, end sequence
sequence = text.find_between('q', 5, 'br')
# >> ['quick br', 'quack br']

entire_text = text.find_between(text.text[0], len(text.text) - 2, text.text[-1])
# >> ['The 6 quick brown foxes jump over 12 lazy dogs 123 times! The ducks quack braveley as the hunter takes his aim.']
