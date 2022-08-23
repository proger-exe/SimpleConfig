from typing import List

class ParseException(Exception):
    pass

def prepare_item(item: str) -> str:
    return item.strip()


def prepare_value(value: str) -> str:
    comment = value.find("//")
    if comment != -1:
        return value[:comment]
    return value


class SimpleConfig:
    def __init__(self, dilimitar: str = "=") -> None:
        self.data = {}
        self.dilimitar = dilimitar

    def update_data(self, field: List[str]) -> None:
        key = field[0]
        value = field[1]
        prepared_key = prepare_item(key)
        delete_comment = prepare_value(value)
        prepared_value = prepare_item(delete_comment)
        self.data.update({prepared_key: prepared_value})

    def parse(self, path: str) -> None:
        with open(path) as file:
            self.base_parse(file.read())

    def base_parse(self, data: str) -> None:
        lines = data.splitlines()
        for field in lines:
            if not field:
                continue
            elif self.dilimitar not in field:
                raise ParseException(f"Line {linex.index(field)} is incorrent!")
            field_ = field.split(self.dilimitar)
            self.update_data(field_)

    def get(self, item: str) -> str:
        return self.data[item]
