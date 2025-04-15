from unittest.mock import patch, mock_open
from src.read_csv_excel import read_csv_file, read_excel_file
import pandas as pd


# Тестирование функции чтения CSV файла.
def test_read_csv_file_success():
    file_path = "path/to/csv/file.csv"
    delimiter = ";"
    expected_data = "id;amount;currency\n1;100;USD\n2;200;EUR"

    with patch("builtins.open", mock_open(read_data=expected_data)):
        result = read_csv_file(file_path, delimiter)

    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[0]["amount"] == "100"
    assert result[0]["currency"] == "USD"
    assert result[1]["id"] == "2"
    assert result[1]["amount"] == "200"
    assert result[1]["currency"] == "EUR"

def test_read_csv_file_file_not_found():
    file_path = "non/existent/file.csv"
    delimiter = ";"

    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_csv_file(file_path, delimiter)

    assert result == []

def test_read_csv_file_exception():
    file_path = "path/to/csv/file.csv"
    delimiter = ";"

    with patch("builtins.open", side_effect=Exception("Some error")):
        result = read_csv_file(file_path, delimiter)

    assert result == []

if __name__ == "__main__":
    test_read_csv_file_success()
    test_read_csv_file_file_not_found()
    test_read_csv_file_exception()


# Тестирование функции чтения Excel файла.
def test_read_excel_file_success():
    file_path = "path/to/excel/file.xlsx"

    expected_data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]

    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame(expected_data)
        result = read_excel_file(file_path)

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[0]["amount"] == 100
    assert result[0]["currency"] == "USD"
    assert result[1]["id"] == 2
    assert result[1]["amount"] == 200
    assert result[1]["currency"] == "EUR"

def test_read_excel_file_file_not_found():
    file_path = "non/existent/file.xlsx"

    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_excel_file(file_path)

    assert result == []

def test_read_excel_file_exception():
    file_path = "path/to/excel/file.xlsx"

    with patch("pandas.read_excel", side_effect=Exception("Some error")):
        result = read_excel_file(file_path)

    assert result == []

if __name__ == "__main__":
    test_read_excel_file_success()
    test_read_excel_file_file_not_found()
    test_read_excel_file_exception()