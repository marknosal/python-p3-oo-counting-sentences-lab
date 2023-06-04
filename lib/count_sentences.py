#!/usr/bin/env python3

# class MyString:
#   def __init__(self, value=''):
#     self.value = value

#   @property
#   def value(self):
#     return self._value
#   @value.setter
#   def value(self, value):
#     if isinstance(value, str):
#       self._value = value
#     else:
#       print('The value must be a string.')

#   def is_sentence(self):
#     if self._value.endswith('.'):
#       return True
#     else:
#       return False
    
#   def is_question(self):
#     return self._value.endswith('?')

class MyString:
    def __init__(self, value=''):
        self.value = value

    def get_value(self):
        return self._value
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print('The value must be a string.')
    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False
    def is_exclamation(self):
        return self._value.endswith('!')
    def count_sentences(self):
        sentence_count = 0
        
        for substring in self._value.split():
            if substring.endswith('.') or substring.endswith('?') or substring.endswith('!'):
                sentence_count += 1

        return sentence_count
    