from src.generators import filter_by_currency, transaction_descriptions,card_number_generator


def test_filter_by_currency(sample_transactions):
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 3
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_transactions)


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions) == 5
    assert all(isinstance(d, str) for d in descriptions)


def test_card_number_generator():
    numbers = list(card_number_generator(1, 5))
    assert numbers == [
        "0000000000000001",
        "0000000000000002",
        "0000000000000003",
        "0000000000000004",
        "0000000000000005"
    ]