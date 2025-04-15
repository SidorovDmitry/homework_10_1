from unittest.mock import patch, mock_open
from src.read_csv_excel import read_csv_file

def test_read_csv_file():
    file_path = "../data/transactions.csv"
    delimiter = ";"

    mocked_open = mock_open(read_data="id;amount;currency\n1;100;USD\n2;200;EUR")
    with patch("builtins.open", mocked_open):


        result = read_csv_file(file_path, delimiter)

    assert len(result) == 2
    assert result[0]["id"] == "1"
    assert result[0]["amount"] == "100"
    assert result[0]["currency"] == "USD"
    assert result[1]["id"] == "2"
    assert result[1]["amount"] == "200"
    assert result[1]["currency"] == "EUR"

if __name__ == "__main__":
    test_read_csv_file()