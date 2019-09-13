from ..string_kata import *


def test_test1_returns_string():
    test1_string = string_is_of_type_string(1234)

    assert str(test1_string)


def test_string_is_reversed():
    reversed_str = reversed_string('Jonathan')

    assert reversed_str == 'nahtanoJ'


def test_string_is_all_caps():
    all_caps_string = all_caps('this is all caps')

    assert all_caps_string == 'THIS IS ALL CAPS'


def test_string_is_all_lowercase():

    lowercase = all_lower_case('JoNaThAn')

    assert lowercase == 'jonathan'


def test_string_get_first_two_charcters():

    characters = string_get_first_two_characters('characters')

    assert 'ch' == characters


def test_string_get_last_two_characters():

    characters = string_get_last_two_characters('characters')

    assert 'rs' == characters


def test_string_get_ever_other_letter_in_string():

    characters = string_get_ever_other_letter_in_string('character')

    assert 'caatr' == characters
