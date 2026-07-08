import pytest
from unittest.mock import patch, MagicMock
from src.api.rest import call_lr
from requests.exceptions import HTTPError

class TestGetCall:
    @patch("src.api.rest.requests.get")
    def test_call_lr_no_cursor(self, mock_get):
        mock_response1 = MagicMock()
        mock_response1.json.return_value = {
            "results": {"results": [{"id": 1}], "cursor": ""}

            }
        mock_get.return_value = mock_response1
        gen = call_lr("http://example.com", "/endpoint", {"cursor": ""}, {})
        result = list(gen)

        assert result == [[{"id": 1}]]

    @patch("src.api.rest.requests.get")
    def test_call_lr_pagination(self, mock_get):
        mock_response1 = MagicMock()
        mock_response1.json.return_value = {
            "results": {"results": [{"id": 1}], "cursor": "abc"}
        }
        mock_response2 = MagicMock()
        mock_response2.json.return_value = {
            "results": {"results": [{"id": 2}], "cursor": "bcd"}
        }
        mock_response3 = MagicMock()
        mock_response3.json.return_value = {
            "results": {"results": [{"id": 3}], "cursor": "bcd"}
        }
        mock_get.side_effect = [mock_response1, mock_response2, mock_response3]

        gen = call_lr("http://example.com", "/endpoint", {"cursor": ""}, {})
        result = list(gen)

        assert result == [[{"id": 1}],[{"id": 2}],[{"id": 3}]]
            
    @patch("src.api.rest.requests.get")
    def test_call_lr_404(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = HTTPError

        mock_get.return_value = mock_response

        with pytest.raises(HTTPError):
            gen = call_lr("http://example.com", "/endpoint", {"cursor": ""}, {})
            result = list(gen)




