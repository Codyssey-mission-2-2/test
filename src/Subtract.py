def subtract(a: int | float, b: int | float) -> int | float:
    """
    a에서 b를 뺀 값을 반환한다.

    Parameters:
        a (int | float): 피감수 (빼지는 수)
        b (int | float): 감수 (빼는 수)

    Returns:
        int | float: a에서 b를 뺀 값

    Raises:
        TypeError: 숫자(int, float)가 아닌 값이 입력된 경우
    """
    for name, value in (("a", a), ("b", b)):

        # bool은 int의 하위 타입이라 별도로 제외한다.

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"{name}는 int 또는 float여야 합니다. (입력된 타입: {type(value).__name__})"
            )
        
    return a - b