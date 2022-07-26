class SimpleConfig:
    def __init__(self) -> None:
        self.data = {}

    def parse(self, path: str) -> None:
        with open(path) as file:
            data = file.readlines()
            for i in data:
                index = i.split(':')
                self.data.update({index[0]: index[1].replace('\n', '').split("//")[0]})

    def get(self, item: str) -> str:
        return self.data[item]
