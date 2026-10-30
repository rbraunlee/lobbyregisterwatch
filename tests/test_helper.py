from helper import flatten_json
from pandas import testing


class TestFlattenJson:
    def test_flatten_list(self, listj, listj_result_df):
        df = flatten_json(listj)
        print("df:")
        print(df)
        print(df.columns, df.index)

        print("listj_result_df:")
        print(listj_result_df)
        print(listj_result_df.columns, listj_result_df.index)
        testing.assert_frame_equal(df, listj_result_df)

    def test_flatten_dict(self, dictj, dictj_result_df):
        df = flatten_json(dictj)
        print("df:")
        print(df)
        print(df.columns, df.index)

        print("listj_result_df:")
        print(dictj_result_df)
        print(dictj_result_df.columns, dictj_result_df.index)
        testing.assert_frame_equal(df, dictj_result_df)

    def test_flatten_dict_list(self, dict_listj, dict_listj_result_df):
        df = flatten_json(dict_listj)
        print("df:")
        print(df)
        print(df.columns, df.index)

        print("listj_result_df:")
        print(dict_listj_result_df)
        print(dict_listj_result_df.columns, dict_listj_result_df.index)
        testing.assert_frame_equal(df, dict_listj_result_df)
