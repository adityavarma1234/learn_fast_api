def get_full_name_str(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int) -> str:
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

def process_item(items: list[str]):
    for item in items:
        print(item)

def process_item1(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

def process_item_dict(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

def process_items_item_str(item: int | str):
    print(item)

def say_hi(name: str | None = None):
    if name is not None:
        print(f"hey {name}")
    else:
        print("Hello World")

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

print(get_full_name_str("john", "doe"))