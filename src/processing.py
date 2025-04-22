def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует транзакции по указанному статусу"""
    # Проверка входных данных
    if not transactions:
        raise ValueError("Передан пустой список транзакций")

    if not isinstance(state, str) or state.upper() not in {"EXECUTED", "CANCELED", "PENDING"}:
        raise ValueError("Недопустимый статус. Допустимые значения: EXECUTED, CANCELED, PENDING")

    state = state.upper()
    filtered_transactions = []

    for transaction in transactions:
        if not isinstance(transaction, dict):
            continue  # Пропускаем некорректные элементы

        # Безопасное получение и преобразование статуса
        transaction_state = transaction.get("state")

        # Преобразуем значение в строку, если оно не None
        if transaction_state is None:
            continue

        try:
            # Пробуем преобразовать в строку (работает для str, int, float)
            transaction_state = str(transaction_state).strip().upper()
        except (AttributeError, TypeError):
            continue  # Пропускаем если не можем преобразовать

        if transaction_state == state:
            filtered_transactions.append(transaction)

    if not filtered_transactions:
        raise ValueError(f"Не найдено транзакций со статусом '{state}'")

    return filtered_transactions


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Функция возвращать новый список, отсортированный по дате"""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)
