import time


def log(filename=None):
    """Декоратор для логирования вызовов функции. Этот декоратор записывает информацию о вызовах обернутой функции,
    включая переданные аргументы и возвращаемое значение, в указанный файл или выводит в консоль.В случае возникновения
    исключения декоратор также записывает информацию об ошибке."""

    def my_decorator(func):
        def inner(*args, **kwargs):

            try:
                print(args)
                result = func(*args, **kwargs)
                message = f"{func.__name__} OK {time.asctime()}\n"
            except Exception as error:
                result = None
                message = f"{func.__name__} {time.asctime()} error: {error}. Inputs: {args}, {kwargs}\n"
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(message)
                else:
                    print(message)

            return result

        return inner

    return my_decorator


@log("log.txt")
def _summ(a, b):
    print(a + b)


_summ(-12, 12)
