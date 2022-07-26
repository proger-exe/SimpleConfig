from typing import List


class SimpleConfig:
    def __init__(self) -> None:
        self.data = {}

    def update_data(self, field: List[str]) -> None:
        key = field[0]
        value = field[1]
        prepared_key = key.strip()
        prepared_value = value.strip().split("//")[0]
        self.data.update({prepared_key: prepared_value})

    def parse(self, path: str) -> None:
        with open(path) as file:
            data = file.readlines()
            for field in data:
                field_ = field.split('=')
                self.update_data(field_)

    def get(self, item: str) -> str:
        return self.data[item]
