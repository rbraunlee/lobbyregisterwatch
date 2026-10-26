from helper import flatten_json


class TestFlattenJson:
    def test_flatten_list(self, listj, listj_result_df):
        df = flatten_json(listj)
        assert df == listj_result_df

    def test_flatten_dict(self, dictj, dictj_result_df):
        df = flatten_json(dictj)
        assert df == dictj_result_df

    def test_flatten_dict_list(self, dict_listj, dict_listj_result_df):
        df = flatten_json(dict_listj)
        assert df == dict_listj_result_df
