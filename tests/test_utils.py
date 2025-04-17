import json
from unittest.mock import mock_open, patch

from src.utils import get_operations_data


@patch("builtins.open")
@patch("json.load")
def test_parse_data(mock_load, mock_open_file):
    mock_open_file.new = mock_open()
    test_json = [{}]
    mock_load.return_value = test_json
    result = get_operations_data("")
    assert result == test_json


@patch("builtins.open")
def test_parse_data_file_not_found(mock_open_file):
    mock_open_file.new = mock_open()
    mock_open_file.side_effect = FileNotFoundError

    result = get_operations_data("")
    assert result == []


@patch("builtins.open")
@patch("json.load")
def test_parse_data_json_decode_error(mock_load, mock_open_file):
    mock_open_file.new = mock_open()
    mock_load.side_effect = json.JSONDecodeError("ERROR", "", 1)
    result = get_operations_data("")
    assert result == []
