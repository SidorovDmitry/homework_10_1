from functools import wraps
from time import ctime


def write_log(message, filename=None):
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            write_log(f"Функция {func.__name__} началась в {ctime()}", filename)
            try:
                result = func(*args, **kwargs)
                write_log(f"Функция {func.__name__} завершилась в {ctime()}", filename)
                return result
            except Exception as e:
                write_log(f"Ошибка в {func.__name__}: {str(e)}", filename)
                raise

        return wrapper

    return decorator
