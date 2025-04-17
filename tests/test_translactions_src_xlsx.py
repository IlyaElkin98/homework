import unittest
from unittest.mock import mock_open, patch
from src.read_files import read_csv_file, read_excel_file
import os


class TestReadCSVFile(unittest.TestCase):
    @patch("csv.reader")
    def test_get_data_from_csv(mock_reader, result):
        mock_reader.return_value = iter(
            [
                ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
                [
                    "650703",
                    "EXECUTED",
                    "2023-09-05T11:30:32Z",
                    "16210",
                    "SoL",
                    "PEN",
                    "Счет 58803664651298323391",
                    "Счет 39746506635466619397",
                    "Перевод организации",
                ],
            ]
        )

        result = read_csv_file(os.path.join("path_to_data", "transactions.csv"))
        expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "SoL",
                "currency_code": "PEN",
                "from": "Счет 58803664651298323391",
                "to": "Счет 39746506635466619397",
                "description": "Перевод организации",
            }
        ]

    def test_file_not_found_csv(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = read_csv_file("transactions.csv")
            self.assertEqual(result, "Файл не найден")

    def test_empty_file_csv(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = read_csv_file("transactions.csv")
            self.assertEqual(result, None)


class TestReadExcelFile(unittest.TestCase):
    def test_get_data_from_xlsx(mock_reader_xlsx):
        mock_reader_xlsx.return_value = iter(
            [
                ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
                [
                    "650703",
                    "EXECUTED",
                    "2023-09-05T11:30:32Z",
                    "16210",
                    "SoL",
                    "PEN",
                    "Счет 58803664651298323391",
                    "Счет 39746506635466619397",
                    "Перевод организации",
                ],
            ]
        )

        result = read_excel_file(os.path.join("path_to_data", "transactions_excel.xlsx"))
        expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "SoL",
                "currency_code": "PEN",
                "from": "Счет 58803664651298323391",
                "to": "Счет 39746506635466619397",
                "description": "Перевод организации",
            }
        ]

    def test_file_not_found_xlsx(self):
        with patch("pandas.read_excel", side_effect=FileNotFoundError):
            result = read_excel_file("transactions.xlsx")
            self.assertEqual(result, "Файл не найден")

    def test_invalid_data_xlsx(self):
        with patch("pandas.read_excel", side_effect=ValueError):
            result = read_excel_file("transactions.xlsx")
            self.assertEqual(result, "Данные отсутствуют или не соответствуют формату")


if __name__ == "__main__":
    unittest.main()
