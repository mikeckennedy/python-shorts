import json
from pathlib import Path
from typing import Iterable


def main():
    sales = load_list()

    count = 10
    for idx, s in enumerate(sales, start=1):
        if idx > count:
            break

        print(f'{idx}. {s.first_name} {s.last_name} bought {s.make} {s.model} for ${s.price:,}.')


class AutoCustomer:
    id: int
    first_name: str
    last_name: str
    email: str
    make: str
    model: str
    year: int
    vin: str
    price: int

    def __init__(self, _id: int, first_name, last_name, email, make, model, year, vin, price):
        # print(f"Creating customer: {first_name} {last_name}")
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price


def load_list() -> Iterable[AutoCustomer]:
    file = Path(__file__).parent / 'MOCK_DATA.json'
    with file.open('r') as fin:
        # Use json-stream package to stream this too.
        # We're just keeping it simple
        raw_data = json.load(fin)

    # customers = []
    # for entry in raw_data:
    #     c = AutoCustomer(**entry)
    #     customers.append(c)

    # customers = [AutoCustomer(**entry) for entry in raw_data]

    customers = (AutoCustomer(**entry) for entry in raw_data)

    return customers


if __name__ == '__main__':
    main()

# htmx + fastapi + tailwind + mongodb
# ACHN https://kivymd.readthedocs.io/en/latest/index.html -
# https://www.youtube.com/channel/UCl72hvzwQ0rXUMBKTsKjRAA
