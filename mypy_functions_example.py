from collections.abc import Iterator, Callable
from typing import Union, Optional

def stringify(num: int) -> str:
    return str(num)

def plus(num1: int, num2: int) -> int:
    return num1 + num2

def show(value: str, excitement: int = 10) -> None:
    print(value + "!" + excitement)

def untyped(x):
    x.anything() + 1 + "string"

x: Callable[[int, float], float] = f
def reigster(callback: Callable[[str], int]) -> None: ...

def getn(N: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1

def second_email(
        address: str | list[str],
        sender: str,
        cc: list[str] | None,
        bcc: list[str] | None,
        subject: str = '',
        body: list[str] | None = None,
) -> bool:
    ...

def quux(x: int, /, * , y:int) -> None:
    pass

quux(3,y=5)
quux(3, 5)
quux(x=3, y=5)


def call(self, *args: str, **kwargs: str) -> str:
    reveal_type(args)
    reveal_type(kwargs)
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)