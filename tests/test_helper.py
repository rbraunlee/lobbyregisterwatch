from helper import flatten_json
from pandas import testing


class TestFlattenJson:
    def test_flatten_list(self, list_df, list_df_result_df):
        df = flatten_json(list_df)
        testing.assert_frame_equal(df, list_df_result_df)

    def test_flatten_dict(self, dictj, dictj_result_df):
        df = flatten_json(dictj)
        testing.assert_frame_equal(df, dictj_result_df)

    def test_flatten_dict_list(self, dict_list_df, dict_list_df_result_df):
        df = flatten_json(dict_list_df)
        print("df:")
        print(df)
        print(df.columns, df.index)

        print("list_df_result_df:")
        print(dict_list_df_result_df)
        print(dict_list_df_result_df.columns, dict_list_df_result_df.index)
        testing.assert_frame_equal(df, dict_list_df_result_df)
