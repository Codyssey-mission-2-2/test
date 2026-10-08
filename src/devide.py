def add(a: int, b: int) -> float | int:
    if type(a) is not int or type(b) is not int:
        raise TypeError("a와 b는 정수만 들어올 수 있습니다.")

    return a / b