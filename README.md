# explicit_re
explicit_re is a python implementation of regex. Its main aim is to be easy to use and readable.

This is a hobby project I'm currently working on that aims to implement regex-like functionality but in a more human readable way. None of these functions actually invoke the existing *re* package (or any other package except *string*). *explicit_re* is meant to be a more explicit way to search text and is nowhere near as compact as regex.

**Example:**

text = 'hello world'

//*explicit_re* invokes a class called Text and passes any string we want to search through it, so for the below *explicit_re* code to work, we would need to do this:

from explicit_re import Text

text = Text('hello world')//

**re:** re.findall("\^hello", text)

\>> \['hello'\]

**explicit_re:** text.starts\_with("hello")

\>> \['hello'\]

**re:** re.findall("he..o", txt)

\>> \['hello'\]

**explicit_re:** text.find\_between("he", 2, "o")

\>> \['hello'\]

This is a special case function that returns a dict of the indexes that the matched sequence begins with:

text = Text('The 6 quick brown foxes jump over 12 lazy dogs 123 times! The ducks quack braveley as the hunter takes his aim.')

**explicit_re:** text.contains\_d('The')

\>> {'The': \[0, 58\]}

In the above example, we can see that the word "The" appears twice in our text, the first instance begins at index 0 (text.text\[0\] = 'T') and at index 58 (text.text\[58\] = 'T').

I will be adding more functionality to this as time goes on. But again, this is only a hobby project and is in no way meant to act as a replacement to the existing *re* package.

# Further Examples:

```python
from explicit_re import Text

text = Text('The 6 quick brown foxes jump over 12 lazy dogs 123 times! The ducks quack braveley as the hunter takes his aim.')

text.starts_with('Th')
# >> ['The']

text.ends_with('dogs')
# >> []

text.contains('The')
# >> ['The', 'The']

#This is a special case function that returns a dict of the indexes that the matched sequence begins with
text.contains_d('The')
# >> {'The': [0, 58]}

# Get characters in text from lowercase n to uppercase T (regex: [n-zA-T])
characters = text.get_characters('n', 'T')
# >> ['T', 'q', 'u', 'r', 'o', 'w', 'n', 'o', 'x', 'u', 'p', 's', 'o', 'v', 'r', 't', 'z', 'y', 'o']

# Get digits
digits = text.get_digits()
# >> ['6', '1', '2', '1', '2', '3']

#Find any sequence that matches the following pattern: start sequence, amount of characters in between, end sequence (In regex: [h...o] >> ['hello'])
sequence = text.find_between('q', 5, 'br')
# >> ['quick br', 'quack br']

entire_text = text.find_between(text.text[0], len(text.text) - 2, text.text[-1])
# >> ['The 6 quick brown foxes jump over 12 lazy dogs 123 times! The ducks quack braveley as the hunter takes his aim.']
```
