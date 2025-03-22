import pytest


@pytest.fixture
def correct_date_string():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def incorrect_date_string_no_time():
    return "11-03-2024"


@pytest.fixture
def incorrect_date_string_wrong_separator():
    return "11.03.2024 02:26:18"


@pytest.fixture
def incorrect_date_string_extra_chars():
    return "2024-03-11T02:26:18.671407Z"


@pytest.fixture
def incorrect_date_string_non_numeric():
    return "2024-03-ABT02:26:18.671407"


@pytest.fixture
def incorrect_date_string_wrong_delimiter():
    return "2024-03-11X02:26:18.671407"


@pytest.fixture
def incorrect_date_string_too_many_parts():
    return "2024-03-11T02:26:18.671407XYZ"


@pytest.fixture
def incorrect_date_string_invalid_month():
    return "2024-13-11T02:26:18.671407"
