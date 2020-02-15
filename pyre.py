import string

class Text:

    def __init__(self, text):
        self.text = text

    def starts_with(self, search_string):

        text = list(self.text)
        text_words = self.text.split(' ')
        search_string = list(search_string)

        for index, letter in enumerate(search_string):
            if letter == text[index]:
                pass
            else:
                return []

        return [text_words[0]]

    def ends_with(self, search_string):

        text = list(self.text)[::-1]
        text_words = self.text.split(' ')
        search_string = list(search_string)[::-1]

        for index, letter in enumerate(search_string):
            if letter == text[index]:
                pass
            else:
                return []

        return [text_words[-1]]

    def contains(self, search_string):

        text = list(self.text)
        indexes = []

        for index, char in enumerate(text):
            res = self.text.find(search_string, index)
            if res == -1 or res in indexes:
                pass
            else:
                indexes.append(res)

        result = [self.text[x:x+len(search_string)] for x in indexes]

        return result

    def contains_d(self, search_string):

        text = list(self.text)
        indexes = []

        for index, char in enumerate(text):
            res = self.text.find(search_string, index)
            if res == -1 or res in indexes:
                pass
            else:
                indexes.append(res)

        result = [self.text[x:x+len(search_string)] for x in indexes]

        result_dict = {search_string: indexes}

        return result_dict

    def get_characters(self, start='a', end='Z'):

        text = list(self.text)
        lowercase_alphabet = string.ascii_lowercase
        uppercase_alphabet = string.ascii_uppercase
        alphabet_list = lowercase_alphabet + uppercase_alphabet

        alphabet_dict = {}

        for index, char in enumerate(alphabet_list):
            alphabet_dict[char] = index

        start_index = alphabet_dict[start]
        end_index = alphabet_dict[end]

        if start_index > end_index:
            temp = start
            start = end
            end = temp

        character_search_list_index = list(range(alphabet_dict[start],alphabet_dict[end] + 1))

        character_search_list = [alphabet_list[x] for x in character_search_list_index]

        result = []

        for char in text:
            if char in character_search_list:
                result.append(char)

        return result

    def get_digits(self):

        text = list(self.text)
        digits = []

        for char in text:
            try:
                int(char)
                digits.append(char)
            except ValueError:
                pass

        return digits

    def find_between(self, start, amount_in_between, end):

        # Loops through and appends all the indexes it finds for the sequences that begin with start
        start_index_list = []

        start_index = int(self.text.find(start))
        start_index_list.append(start_index)

        for char in self.text:
            start_index = int(self.text.find(start, start_index_list[-1] + 1))
            if start_index == -1:
                break
            else:
                start_index_list.append(start_index)

        result = []

        for index in start_index_list:
            end_index = index + amount_in_between + 1
            end_length = len(end)
            if self.text.find(end, end_index) == end_index:
                result.append(self.text[index:end_index + end_length])

        return result
