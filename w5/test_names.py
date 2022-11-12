from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full():
    assert make_full_name('Sally','Brown') == 'Brown; Sally'
    assert make_full_name('Ty','Blot') == 'Blot; Ty'
    assert make_full_name('Longfirstname','Shaq-ONeil') == 'Shaq-ONeil; Longfirstname'

def test_extract_family():
    assert extract_family_name('Brown; Sally') == 'Brown'
    assert extract_family_name('Blot; Ty') == 'Blot'
    assert extract_family_name('Shaq-ONeil; Longfirstname') == 'Shaq-ONeil'

def test_extract_given_name():
    assert extract_given_name('Brown; Sally') == 'Sally'
    assert extract_given_name('Hanis; Nate') == 'Nate'
    assert extract_given_name('Birch; Larry-Nash') == 'Larry-Nash'


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])