class User:
    def __init__(self, line: str) -> None:
        self.id, self.favourites, self.age, self.email = line.strip().split(", ")
        self.favourites = self.favourites.split(" ")
        self.age = int(self.age)