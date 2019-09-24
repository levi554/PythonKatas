from ..dict_kata import verify_this_is_dict


def test_create_dict_from_string():

    verify_dict = verify_this_is_dict('Jonathan')

    assert type(verify_dict) is dict


def test_create_dict_from_list():

    new_dict = create_dict_from_list(['Jonathan', 'Livesay', 1, 2, 3])

    assert new_dict is {'firstname': 'Jonathan', 'lastname': 'Livesay', 'value1': 1, 'value2': 2, 'value3': 3}