import sys

sys.set_int_max_str_digits(1000000000)


def mulmatrix2x1(a: (int, int), b: (int, int, int, int)) -> (int, int):
    """
    returns result of the multiplication of 2x2 and 2x1

    Parameters:
        a (tuple[int, int, int, int]): a first matrix
        b (tuple[int, int, int, int]): a second matrix

    Returns:
        multiplication (tuple[int, int]): a * b
    """
    return a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3]


def mulmatrix2x2(a: (int, int, int, int), b: (int, int, int, int)) -> (int, int, int, int):
    """
    returns the product of multiplication of two 2x2 matrices: a * b

    Parameters:
         a (tuple[int, int, int, int]): a first matrix
         b (tuple[int, int, int, int]): a second matrix

        Returns:
            multiplication (tuple[int, int, int, int]): a * b
    """
    return a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3], a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3]


def fibonacci(n: int) -> (int, int):
    """
    count n- fibonacci number

    Parameters:
        n (int) - order number

    Returns:
        fibonacci number
    """
    a = (0, 1, 1, 1)
    b = (1, 0, 0, 1)

    while n > 0:
        if n % 2 == 1:
            b = mulmatrix2x2(b, a)
        n //= 2
        a = mulmatrix2x2(a, a)

    return mulmatrix2x1((0, 1), b)


def main(n: str):
    if not str(n).isnumeric():
        raise ValueError("n должно быть натуральным числом")

    return {'result': str(fibonacci(int(n))[0])}


if __name__ == '__main__':
    print(main(input("n:")))
