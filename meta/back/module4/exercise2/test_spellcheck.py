''' 
Import statements: 
    1. Import pytest and spellcheck modules
'''

import pytest
import spellcheck

alpha = "Checking the length & structure of the sentence."

@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.
    """
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50

    #2 asserts

# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.
    """
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value).endswith(".")

