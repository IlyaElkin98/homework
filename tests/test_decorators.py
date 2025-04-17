from src.decorators import log


def test_log():

    @log("log.txt")
    def add_numbers(a, b):
        return a + b

    result1 = add_numbers(3, 5)
    assert result1 == 8

    @log("log.txt")
    def sub_numbers(a, b):
        return a - b

    result2 = sub_numbers(21, 4)
    assert result2 == 17
