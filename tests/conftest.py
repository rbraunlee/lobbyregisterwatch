import sys
import os
import pandas as pd
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


@pytest.fixture
def first_json():
    return '{"key_one":{"key_two":"value_one", "key_three":"value_two"}, "key_four":"value_three"}'


@pytest.fixture
def second_json():
    return '{"key_one":{"key_two":"new_value_one", "key_three":"value_two"}, "key_four":"new_value_three"}'


@pytest.fixture
def listj():
    return '{ "key_one":["value1", "value2", "value3"]}'


@pytest.fixture
def listj_result_df():

    return pd.DataFrame({"key_one": ["value1", "value2", "value3"]})


@pytest.fixture
def dictj():
    return '{"key_one":{ "key_j1" :"value1", "key_j2":"value2", "key_j3":"value3"}}'


@pytest.fixture
def dictj_result_df():

    return pd.DataFrame(
        {"key_one_key_j1": ["value1"], "key_one_key_j2": ["value2"], "key_one_key_j3": ["value3"]}
    )


@pytest.fixture
def dict_listj():
    return '{"key_one":{"key_list":{"key_j1":"hi", "key_j2":["value1", "value2", "value3"], "key_j3":"by"}}}'


@pytest.fixture
def dict_listj_result_df():

    return pd.DataFrame(
        {
            "key_one_key_list_key_j1": ["hi", "hi", "hi"],
            "key_one_key_list_key_j2": ["value1", "value2", "value3"],
            "key_one_key_list_key_j3": ["by", "by", "by"],
        }
    )
