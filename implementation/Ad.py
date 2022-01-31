class Ad: 
    def __init__(self, line: str) -> None:
        self.id, self.price, self.owner = line.strip().split(", ")