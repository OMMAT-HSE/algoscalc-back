import sys

sys.set_int_max_str_digits(1000000000)

def mulmatrix2x2(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    """
    returns the product of multiplication of two 2x2 matrices: a * b

        Parameters:
            a (tuple[int, int, int, int]): a first matrix
            b (tuple[int, int, int, int]): a second matrix

        Returns:
            multiplication (tuple[int, int, int, int]): a * b
    """
    return a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3], a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3]


def mulmatrix2x1(a: tuple[int, int], b: tuple[int, int, int, int]) -> tuple[int, int]:
    return a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3]


def fibonacci(n: int) -> int:
    a = (0, 1, 1, 1)
    b = (1, 0, 0, 1)
    while n > 0:
        if n % 2 == 1:
            b = mulmatrix2x2(b, a)
        n //= 2
        a = mulmatrix2x2(a, a)
    return mulmatrix2x1((0, 1), b)


def check(n: int) -> None:
    if n < 1:
        raise ValueError("n должно быть больше 0")


def main(n: str):
    try:
        N = int(n)
    except ValueError:
        raise ValueError("n должно быть целым числом")
    check(N)
    return {'result': str(fibonacci(N)[0])}


if __name__ == '__main__':
    print(main(input("n:")))
