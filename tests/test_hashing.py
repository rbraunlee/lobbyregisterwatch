from hashing import has_changed, hash_content

class TestHashContent:
    def test_hash_content_same_(self, first_json):
        hashed_content = hash_content(first_json)
        hashed_content_two = hash_content(first_json)
        assert hashed_content == hashed_content_two

    def test_has_content_diff_input(self, first_json, second_json):
        hashed_content = hash_content(first_json)
        hashed_content_two = hash_content(second_json)
        assert hashed_content != hashed_content_two

    def test_has_content_return_str(self, first_json):
        hashed_content = hash_content(first_json)
        assert isinstance(hashed_content, str)


class TestHasChanged:
    def test_has_changed_no_hash(self, first_json):
        value = has_changed(first_json, None)
        assert value is True

    def test_has_changed_not(self, first_json):
        pre_value = hash_content(first_json)
        value = has_changed(first_json, pre_value)
        assert value is False

    def test_has_changed_true(self, first_json, second_json):
        pre_value = hash_content(first_json)
        value = has_changed(second_json, pre_value)
        assert value is True



