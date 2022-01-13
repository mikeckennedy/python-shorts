import json
from pathlib import Path


def main():
    sales: list[AutoCustomer] = load_list()

    by_email: dict[str, AutoCustomer] = {}
    by_vin: dict[str, AutoCustomer] = {}
    unique_vins: set[str] = set()

    email = input("Do a search by email: ")
    sale = by_email.get(email)
    print(sale)

    print()
    vin = input("Do a search by vin: ")
    sale = by_vin.get(vin)
    print(sale)

    print()
    input("Enter to continue...")
    print(unique_vins)
    print(f'Number of unique vins: {len(unique_vins)} out of {len(sales):,} sales')


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
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price

    def __repr__(self):
        return f'<{self.email} bought {self.make} {self.model} ({self.vin}) for ${self.price:,}>'

    def __str__(self):
        return repr(self)


def load_list() -> list[AutoCustomer]:
    return [AutoCustomer(**entry) for entry in (load_data())]


def load_data():
    file = Path(__file__).parent / 'MOCK_DATA.json'
    with file.open('r') as fin:
        # Use json-stream package to stream this too.
        # We're just keeping it simple
        raw_data = json.load(fin)
    return raw_data


if __name__ == '__main__':
    main()
