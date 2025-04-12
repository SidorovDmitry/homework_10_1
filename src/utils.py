import json
import logging
import os

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "../logs", "utils.log"), mode="w", encoding="utf-8"
)


file_formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")


# Получаем путь к текущему скрипту
script_dir = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к файлу относительно текущего скрипта
file_path = os.path.join(script_dir, "../data/operations.json")


def read_file(filename=None):
    """Функция для чтения JSON-файла и обработки возможных ошибок при его открытии и чтении"""
    logger.info(read_file.__doc__)
    try:

        with open(filename, "r", encoding="utf-8") as f:
            logger.info("Открытие JSON-файла")
            data = json.load(f)

        # Проверяем, что данные представляют собой список
        if not isinstance(data, list):
            logger.error("Ошибка обработки файла")
            return []

        return data
    except FileNotFoundError as e:
        logger.error(f"Файл не найден {e}")
        print(f"Файл не найден по пути: {filename}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при декодировании JSON из файла {e}")
        print(f"Ошибка при декодировании JSON из файла: {filename}")
        return []
