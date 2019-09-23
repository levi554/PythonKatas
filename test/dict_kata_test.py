from ..dict_kata import * 

def test_create_dict_from_string():

    verify_dict = verify_this_is_dict('Jonathan')

    assert verify_dict == {'firstname': 'Jonathan' }
