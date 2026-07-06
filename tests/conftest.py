import sys
import os
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

@pytest.fixture
def first_json():
    return '{"key_one":{"key_two":"value_one", "key_three":"value_two"}, "key_four":"value_three"}'

@pytest.fixture
def second_json():
    return '{"key_one":{"key_two":"new_value_one", "key_three":"value_two"}, "key_four":"new_value_three"}'


