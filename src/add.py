def add(a: int, b: int) -> int:
    if type(a) is not int or type(b) is not int:
        raise TypeError("a와 b는 정수여야 합니다.")

    return a + b